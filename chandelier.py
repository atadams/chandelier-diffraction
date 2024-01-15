from diffractsim import ApertureFromImage, Lens, MonochromaticField, PolychromaticField, mm, cm, cf, nm, set_backend

set_backend("CPU")  # Change the string to "CUDA" to use GPU acceleration


F = PolychromaticField(
    spectrum=1.5 * cf.illuminant_d65,
    extent_x=27.0 * mm,
    extent_y=27.0 * mm,
    Nx=2000,
    Ny=2000,
)

F.add(ApertureFromImage("./apertures/mts-stagger-2.png", image_size=(20 * mm, 20 * mm), simulation=F))

F.add(Lens(f=45 * cm))
F.propagate(35 * cm)
F.add(ApertureFromImage("./apertures/square.png", image_size=(5 * mm, 5 * mm), simulation=F))
F.propagate(10 * cm)

rgb = F.get_colors()
F.plot_colors(rgb, xlim=[-6 * mm, 6 * mm], ylim=[-6 * mm, 6 * mm], figsize=(10, 10))
