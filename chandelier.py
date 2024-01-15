from diffractsim import ApertureFromImage, Lens, PolychromaticField, cf, cm, mm, set_backend

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
F.plot_colors(rgb, xlim=[-4 * mm, 4 * mm], ylim=[-4 * mm, 4 * mm], figsize=(10, 10))
