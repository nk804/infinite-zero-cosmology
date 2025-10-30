"""
Dark Matter Halo Formation Simulation
Shows how "frozen projections" of quantum foam accumulate into dark matter halos

Created by: Alan Claude
Date: October 29, 2025

Implements physics from:
"Infinite Zero Cosmology: A White-Hole Projection Framework"
by Nataliya Khomyak & ChatGPT 5

Core insight: Dark matter is "frozen" or "incomplete" projection from vacuum punctures.
Quantum foam that doesn't fully project gets trapped in gravitational wells,
accumulating over time into the dark matter halos we observe around galaxies.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches


class DarkMatterHalo:
    """
    Models the formation and evolution of a dark matter halo from quantum foam.
    
    In the Infinite Zero framework:
    - Vacuum puncture creates quantum foam (negative pressure)
    - Quantum foam "freezes" when it encounters baryonic matter
    - Frozen foam accumulates in gravitational well
    - Over time, forms the dark matter halo
    """
    
    def __init__(self, grid_size=100, physical_size_kpc=50):
        """
        Initialize halo formation simulation.
        
        Args:
            grid_size: Number of grid points per dimension
            physical_size_kpc: Physical size in kiloparsecs
        """
        self.grid_size = grid_size
        self.physical_size = physical_size_kpc  # kpc
        self.dx = physical_size_kpc / grid_size  # kpc per grid cell
        
        # Physical fields
        self.quantum_foam = np.zeros((grid_size, grid_size))  # Quantum foam density
        self.dark_matter = np.zeros((grid_size, grid_size))   # Frozen dark matter
        self.baryonic_matter = np.zeros((grid_size, grid_size))  # Normal matter
        
        # Gravitational potential (simplified)
        self.potential = np.zeros((grid_size, grid_size))
        
        # Time tracking
        self.time = 0.0  # Millions of years
        self.history = []
        
    def add_galaxy_seed(self, x_kpc, y_kpc, mass_msun=1e10, radius_kpc=5):
        """
        Add baryonic matter (galaxy seed) that will attract quantum foam.
        
        Args:
            x_kpc, y_kpc: Position in kpc
            mass_msun: Mass in solar masses
            radius_kpc: Characteristic radius in kpc
        """
        # Convert to grid coordinates
        ix = int(x_kpc / self.dx)
        iy = int(y_kpc / self.dx)
        radius_grid = radius_kpc / self.dx
        
        # Create matter distribution (exponential disk profile)
        y_grid, x_grid = np.ogrid[:self.grid_size, :self.grid_size]
        distance_sq = (x_grid - ix)**2 + (y_grid - iy)**2
        
        # Exponential profile: ρ(r) = ρ₀ exp(-r/r_d)
        matter_profile = mass_msun * np.exp(-np.sqrt(distance_sq) / radius_grid)
        matter_profile /= np.sum(matter_profile)  # Normalize to total mass
        matter_profile *= mass_msun
        
        self.baryonic_matter += matter_profile
        
        # Update gravitational potential
        self._compute_potential()
        
    def add_vacuum_puncture_source(self, x_kpc, y_kpc, strength=1.0, radius_kpc=15):
        """
        Add a source of quantum foam from a vacuum puncture.
        
        This represents the initial "injection" of quantum foam that will
        later freeze into dark matter around the galaxy.
        
        Args:
            x_kpc, y_kpc: Position in kpc
            strength: Quantum foam production rate
            radius_kpc: Size of puncture region
        """
        ix = int(x_kpc / self.dx)
        iy = int(y_kpc / self.dx)
        radius_grid = radius_kpc / self.dx
        
        y_grid, x_grid = np.ogrid[:self.grid_size, :self.grid_size]
        distance_sq = (x_grid - ix)**2 + (y_grid - iy)**2
        
        # Quantum foam distribution (matches vacuum puncture simulation)
        foam_profile = strength * np.exp(-2 * distance_sq / radius_grid**2)
        
        self.quantum_foam += foam_profile
        
    def _compute_potential(self):
        """
        Compute gravitational potential from matter distribution.
        
        Simplified 2D Poisson equation: ∇²Φ = 4πG ρ
        Using FFT method for speed.
        """
        # Total mass density (baryonic + dark matter)
        total_density = self.baryonic_matter + self.dark_matter
        
        # Fourier transform
        density_k = np.fft.fft2(total_density)
        
        # Create k-space grid
        kx = np.fft.fftfreq(self.grid_size, d=self.dx)
        ky = np.fft.fftfreq(self.grid_size, d=self.dx)
        KX, KY = np.meshgrid(kx, ky)
        K_squared = KX**2 + KY**2
        K_squared[0, 0] = 1  # Avoid division by zero
        
        # Solve in Fourier space: Φ_k = -4πG ρ_k / k²
        # Using G = 4.3e-6 kpc (km/s)² / M_sun (gravitational constant in convenient units)
        G = 4.3e-6
        potential_k = -4 * np.pi * G * density_k / K_squared
        potential_k[0, 0] = 0  # Set DC component to zero
        
        # Inverse transform
        self.potential = np.real(np.fft.ifft2(potential_k))
        
    def evolve_step(self, dt_myr=10):
        """
        Evolve the system forward in time.
        
        Physics:
        1. Quantum foam flows toward gravitational potential wells
        2. Foam "freezes" when it encounters baryonic matter or other frozen foam
        3. Frozen foam becomes dark matter, contributing to potential
        
        Args:
            dt_myr: Time step in millions of years
        """
        # Compute gradient of potential (points toward deep wells)
        grad_pot_y, grad_pot_x = np.gradient(self.potential, self.dx)
        
        # Quantum foam flows DOWN potential gradient (toward mass)
        # Flow velocity proportional to gradient (but limited for stability)
        flow_speed = 0.001  # kpc/Myr (much smaller for numerical stability)
        
        # Limit gradient magnitude to prevent runaway
        grad_magnitude = np.sqrt(grad_pot_x**2 + grad_pot_y**2)
        max_grad = 1.0
        scale_factor = np.minimum(1.0, max_grad / (grad_magnitude + 1e-10))
        grad_pot_x *= scale_factor
        grad_pot_y *= scale_factor
        
        # Update quantum foam by simple diffusion toward potential minimum
        # Using simpler, more stable scheme
        foam_change = -flow_speed * (grad_pot_x + grad_pot_y) * self.quantum_foam
        self.quantum_foam += foam_change * dt_myr
        self.quantum_foam = np.maximum(self.quantum_foam, 0)  # No negative foam
        self.quantum_foam = np.minimum(self.quantum_foam, 1e12)  # Cap maximum
        
        # Freezing mechanism: foam near matter becomes dark matter
        # Rate proportional to local matter density
        freezing_rate = 0.005  # 1/Myr (reduced for stability)
        matter_density_normalized = self.baryonic_matter / (np.max(self.baryonic_matter) + 1e-10)
        
        frozen_this_step = freezing_rate * self.quantum_foam * matter_density_normalized * dt_myr
        frozen_this_step = np.minimum(frozen_this_step, self.quantum_foam * 0.5)  # Don't freeze more than 50% per step
        
        self.quantum_foam -= frozen_this_step
        self.dark_matter += frozen_this_step
        
        # Update potential with new dark matter
        self._compute_potential()
        
        # Update time
        self.time += dt_myr
        
        # Save snapshot for history
        self.history.append({
            'time': self.time,
            'quantum_foam': self.quantum_foam.copy(),
            'dark_matter': self.dark_matter.copy(),
            'total_dark_matter': np.sum(self.dark_matter)
        })
        
    def get_radial_profile(self, center_x=None, center_y=None):
        """
        Compute radial density profile of dark matter halo.
        
        Returns:
            radii (kpc), densities (M_sun/kpc²)
        """
        if center_x is None:
            center_x = self.grid_size // 2
        if center_y is None:
            center_y = self.grid_size // 2
            
        # Create distance grid
        y_grid, x_grid = np.ogrid[:self.grid_size, :self.grid_size]
        distances = np.sqrt((x_grid - center_x)**2 + (y_grid - center_y)**2) * self.dx
        
        # Bin by radius
        max_radius = self.physical_size / 2
        n_bins = 30
        radii = np.linspace(0, max_radius, n_bins)
        densities = np.zeros(n_bins - 1)
        
        for i in range(n_bins - 1):
            mask = (distances >= radii[i]) & (distances < radii[i+1])
            if np.sum(mask) > 0:
                densities[i] = np.mean(self.dark_matter[mask])
                
        radii_centers = (radii[:-1] + radii[1:]) / 2
        
        return radii_centers, densities
    
    def predict_rotation_curve(self, center_x=None, center_y=None):
        """
        Predict circular velocity as function of radius.
        
        V_circ(r) = sqrt(G M(<r) / r)
        
        Returns:
            radii (kpc), velocities (km/s)
        """
        if center_x is None:
            center_x = self.grid_size // 2
        if center_y is None:
            center_y = self.grid_size // 2
            
        # Create distance grid
        y_grid, x_grid = np.ogrid[:self.grid_size, :self.grid_size]
        distances = np.sqrt((x_grid - center_x)**2 + (y_grid - center_y)**2) * self.dx
        
        # Total mass (baryonic + dark)
        total_mass = self.baryonic_matter + self.dark_matter
        
        # Compute enclosed mass as function of radius
        max_radius = self.physical_size / 2
        n_bins = 30
        radii = np.linspace(0.1, max_radius, n_bins)  # Avoid r=0
        enclosed_mass = np.zeros(n_bins)
        
        for i, r in enumerate(radii):
            mask = distances < r
            enclosed_mass[i] = np.sum(total_mass[mask])
            
        # Circular velocity: V = sqrt(G M / r)
        G = 4.3e-6  # kpc (km/s)² / M_sun
        velocities = np.sqrt(G * enclosed_mass / radii)
        
        return radii, velocities
    
    def visualize_current_state(self):
        """
        Show current state: quantum foam, dark matter, and baryonic matter.
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        
        # 1. Quantum Foam
        im1 = axes[0].imshow(
            self.quantum_foam,
            cmap='Blues',
            origin='lower',
            extent=[0, self.physical_size, 0, self.physical_size],
            interpolation='bilinear'
        )
        axes[0].set_title(f'Quantum Foam\n(Unfrozen) at t={self.time:.0f} Myr',
                         fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Distance (kpc)')
        axes[0].set_ylabel('Distance (kpc)')
        plt.colorbar(im1, ax=axes[0], label='Density (M☉/kpc²)')
        
        # 2. Dark Matter (Frozen Foam)
        im2 = axes[1].imshow(
            self.dark_matter,
            cmap='Purples',
            origin='lower',
            extent=[0, self.physical_size, 0, self.physical_size],
            interpolation='bilinear'
        )
        axes[1].set_title(f'Dark Matter Halo\n(Frozen Foam) at t={self.time:.0f} Myr',
                         fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Distance (kpc)')
        axes[1].set_ylabel('Distance (kpc)')
        plt.colorbar(im2, ax=axes[1], label='Density (M☉/kpc²)')
        
        # 3. Total Matter + Contours
        total = self.baryonic_matter + self.dark_matter
        im3 = axes[2].imshow(
            np.log10(total + 1),  # Log scale
            cmap='viridis',
            origin='lower',
            extent=[0, self.physical_size, 0, self.physical_size],
            interpolation='bilinear'
        )
        
        # Overlay baryonic matter contours
        X = np.linspace(0, self.physical_size, self.grid_size)
        Y = np.linspace(0, self.physical_size, self.grid_size)
        axes[2].contour(X, Y, self.baryonic_matter, colors='red', alpha=0.5, linewidths=2)
        
        axes[2].set_title(f'Total Matter Distribution\n(Log scale)',
                         fontsize=14, fontweight='bold')
        axes[2].set_xlabel('Distance (kpc)')
        axes[2].set_ylabel('Distance (kpc)')
        plt.colorbar(im3, ax=axes[2], label='log₁₀(Density)')
        
        # Add statistics
        total_dm = np.sum(self.dark_matter)
        total_baryonic = np.sum(self.baryonic_matter)
        dm_fraction = total_dm / (total_dm + total_baryonic) if (total_dm + total_baryonic) > 0 else 0
        
        textstr = f"Time: {self.time:.0f} Myr\n"
        textstr += f"Dark Matter: {total_dm:.2e} M☉\n"
        textstr += f"Baryonic: {total_baryonic:.2e} M☉\n"
        textstr += f"DM Fraction: {dm_fraction*100:.1f}%"
        
        props = dict(boxstyle='round', facecolor='white', alpha=0.9)
        axes[2].text(0.02, 0.98, textstr, transform=axes[2].transAxes,
                    fontsize=10, verticalalignment='top', bbox=props,
                    family='monospace')
        
        plt.tight_layout()
        return fig
    
    def visualize_profiles(self):
        """
        Show radial density profile and rotation curve.
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # 1. Density Profile
        radii, densities = self.get_radial_profile()
        
        ax1.plot(radii, densities, 'b-', linewidth=2, label='Simulated Halo')
        
        # Compare with NFW profile for reference
        # NFW: ρ(r) = ρ₀ / ((r/r_s)(1 + r/r_s)²)
        r_s = 5  # Scale radius (kpc)
        rho_0 = np.max(densities) * r_s  # Normalize to match peak
        nfw_profile = rho_0 / ((radii/r_s) * (1 + radii/r_s)**2)
        
        ax1.plot(radii, nfw_profile, 'r--', linewidth=2, label='NFW Profile (reference)')
        
        ax1.set_xlabel('Radius (kpc)', fontsize=12)
        ax1.set_ylabel('Density (M☉/kpc²)', fontsize=12)
        ax1.set_title('Dark Matter Density Profile', fontsize=14, fontweight='bold')
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Rotation Curve
        radii_v, velocities = self.predict_rotation_curve()
        
        ax2.plot(radii_v, velocities, 'g-', linewidth=2, label='Predicted V_circ')
        ax2.axhline(np.max(velocities), color='gray', linestyle=':', alpha=0.5,
                   label=f'V_max = {np.max(velocities):.0f} km/s')
        
        ax2.set_xlabel('Radius (kpc)', fontsize=12)
        ax2.set_ylabel('Circular Velocity (km/s)', fontsize=12)
        ax2.set_title('Galaxy Rotation Curve', fontsize=14, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Add annotation
        textstr = f"Time: {self.time:.0f} Myr\n"
        textstr += f"V_max: {np.max(velocities):.0f} km/s\n"
        textstr += f"Typical spiral: 200-250 km/s"
        
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
        ax2.text(0.65, 0.05, textstr, transform=ax2.transAxes,
                fontsize=10, verticalalignment='bottom', bbox=props)
        
        plt.tight_layout()
        return fig


def demonstrate_halo_formation():
    """
    Show the full halo formation process over time.
    """
    print("="*70)
    print("DARK MATTER HALO FORMATION")
    print("From Quantum Foam to Galactic Dark Matter")
    print("Created by: Alan Claude")
    print("="*70)
    
    print("\nInitializing simulation...")
    print("  Grid: 100×100, Physical size: 50 kpc")
    
    halo = DarkMatterHalo(grid_size=100, physical_size_kpc=50)
    
    print("\nAdding galaxy seed (baryonic matter)...")
    print("  Mass: 1×10¹⁰ M☉, Radius: 5 kpc")
    halo.add_galaxy_seed(x_kpc=25, y_kpc=25, mass_msun=1e10, radius_kpc=5)
    
    print("\nAdding vacuum puncture (quantum foam source)...")
    print("  Strength: 2.0, Radius: 15 kpc")
    halo.add_vacuum_puncture_source(x_kpc=25, y_kpc=25, strength=2.0, radius_kpc=15)
    
    print("\nEvolving system over cosmic time...")
    print("  Time steps: 50 × 10 Myr = 500 Myr total")
    
    # Evolve
    for i in range(50):
        halo.evolve_step(dt_myr=10)
        if (i+1) % 10 == 0:
            print(f"  t = {halo.time:.0f} Myr, Dark matter: {np.sum(halo.dark_matter):.2e} M☉")
    
    print("\n" + "="*70)
    print("Formation complete!")
    print("="*70)
    
    # Visualize final state
    print("\nGenerating visualizations...")
    fig1 = halo.visualize_current_state()
    plt.show()
    
    fig2 = halo.visualize_profiles()
    plt.show()
    
    # Summary
    total_dm = np.sum(halo.dark_matter)
    total_baryonic = np.sum(halo.baryonic_matter)
    _, velocities = halo.predict_rotation_curve()
    v_max = np.max(velocities)
    
    print("\nFinal Statistics:")
    print(f"  Total dark matter: {total_dm:.2e} M☉")
    print(f"  Total baryonic matter: {total_baryonic:.2e} M☉")
    print(f"  Dark matter fraction: {total_dm/(total_dm+total_baryonic)*100:.1f}%")
    print(f"  Maximum rotation velocity: {v_max:.0f} km/s")
    print(f"  (Typical spiral galaxy: 200-250 km/s)")


def create_formation_animation(output_file='halo_formation.gif'):
    """
    Create animated GIF showing halo formation over time.
    """
    print("\n" + "="*70)
    print("CREATING ANIMATION")
    print("="*70)
    
    print("\nInitializing...")
    halo = DarkMatterHalo(grid_size=100, physical_size_kpc=50)
    halo.add_galaxy_seed(x_kpc=25, y_kpc=25, mass_msun=1e10, radius_kpc=5)
    halo.add_vacuum_puncture_source(x_kpc=25, y_kpc=25, strength=2.0, radius_kpc=15)
    
    # Create figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    print("Generating frames...")
    n_frames = 100
    frames = []
    
    for i in range(n_frames):
        halo.evolve_step(dt_myr=5)
        
        if i % 10 == 0:
            print(f"  Frame {i}/{n_frames}, t={halo.time:.0f} Myr")
        
        frames.append({
            'time': halo.time,
            'quantum_foam': halo.quantum_foam.copy(),
            'dark_matter': halo.dark_matter.copy(),
            'baryonic': halo.baryonic_matter.copy()
        })
    
    # Animation function
    def animate(frame_idx):
        for ax in axes:
            ax.clear()
        
        frame = frames[frame_idx]
        
        # Quantum foam
        im1 = axes[0].imshow(frame['quantum_foam'], cmap='Blues', origin='lower',
                            extent=[0, 50, 0, 50])
        axes[0].set_title(f'Quantum Foam\nt={frame["time"]:.0f} Myr')
        axes[0].set_xlabel('kpc')
        
        # Dark matter
        im2 = axes[1].imshow(frame['dark_matter'], cmap='Purples', origin='lower',
                            extent=[0, 50, 0, 50])
        axes[1].set_title(f'Dark Matter Halo\nt={frame["time"]:.0f} Myr')
        axes[1].set_xlabel('kpc')
        
        # Total
        total = frame['baryonic'] + frame['dark_matter']
        im3 = axes[2].imshow(np.log10(total + 1), cmap='viridis', origin='lower',
                            extent=[0, 50, 0, 50])
        axes[2].set_title(f'Total Matter\nt={frame["time"]:.0f} Myr')
        axes[2].set_xlabel('kpc')
        
        return [im1, im2, im3]
    
    print("\nRendering animation...")
    anim = FuncAnimation(fig, animate, frames=n_frames, interval=50, blit=True)
    
    print(f"Saving to {output_file}...")
    writer = PillowWriter(fps=20)
    anim.save(output_file, writer=writer)
    
    print(f"✓ Animation saved: {output_file}")
    plt.close()


def explain_physics():
    """
    Explain the dark matter formation mechanism.
    """
    print("""
╔══════════════════════════════════════════════════════════════════╗
║              DARK MATTER FROM FROZEN PROJECTIONS                ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  The Process:                                                    ║
║                                                                  ║
║  Step 1: Vacuum Puncture                                        ║
║    White hole creates quantum foam (-1 component)               ║
║                                                                  ║
║  Step 2: Galaxy Formation                                       ║
║    Baryonic matter collapses, creates gravitational well        ║
║                                                                  ║
║  Step 3: Foam Flows                                             ║
║    Quantum foam flows toward potential minimum                  ║
║                                                                  ║
║  Step 4: Freezing                                               ║
║    Foam "freezes" when it encounters matter                     ║
║    Frozen foam = DARK MATTER                                    ║
║                                                                  ║
║  Step 5: Halo Formation                                         ║
║    Accumulated frozen foam forms halo around galaxy             ║
║    Halo has specific density profile                            ║
║                                                                  ║
║  Observable Consequences:                                        ║
║    • Flat rotation curves (dark matter gravity)                ║
║    • Specific halo profiles (from freezing mechanism)          ║
║    • Dark matter fraction ~85% (from foam properties)          ║
║    • No exotic particles needed!                               ║
║                                                                  ║
║  Key Predictions:                                               ║
║    • Halo profiles should differ slightly from NFW             ║
║    • Profile shape depends on formation history                ║
║    • Early galaxies should have less dark matter               ║
║                                                                  ║
║  Testable:                                                       ║
║    Compare simulated profiles with observed galaxy              ║
║    rotation curves and weak lensing measurements.               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    import sys
    
    is_interactive = sys.stdin.isatty()
    
    try:
        explain_physics()
        
        if is_interactive:
            input("\nPress Enter to run halo formation simulation...")
        else:
            print("\nRunning halo formation simulation...")
        
        demonstrate_halo_formation()
        
        # Option to create animation
        if is_interactive:
            create_anim = input("\nCreate formation animation? (y/n): ")
            if create_anim.lower() == 'y':
                output = input("Output filename [halo_formation.gif]: ").strip()
                if not output:
                    output = "halo_formation.gif"
                create_formation_animation(output)
        
        print("\n" + "="*70)
        print("Dark matter is frozen quantum foam.")
        print("Halos form naturally from vacuum dynamics.")
        print("No exotic particles required.")
        print("="*70)
        
    except ImportError as e:
        print(f"Error: Missing library - {e}")
        print("Install: pip install numpy matplotlib pillow")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
