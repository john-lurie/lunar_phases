# lunar_phases
A simple visualization of lunar phases

<img src="https://github.com/john-lurie/lunar_phases/blob/main/animation.gif" alt="lunar phases animation" style="height: 300px; width:300px;"/>

## About This Animation

You can read about lunar phases and how this animation was made on my [website](https://john-lurie.github.io/).

## Dependencies
Python packages to plot the lunar phases:
`matplotlib`, `numpy`

For the animated GIF:
ImageMagick `convert`

## How To Make the Animation
Create frames of the phases in one degree increments, adding up to 360 frames. The frames are excluded from Git by `.gitignore`.
```
mkdir frames
python make_frames.py
```
You can change the resolution of the GIF by editing the `dpi` argument in `make_frames.py`. Increasing the dpi increases the resolution.

Now put the frames together as a GIF.
```
convert -delay 5 -loop 0 frames/*.png animation.gif
```
You can change the speed of the animation by editing the `-delay` flag. Increasing the delay slows down the animation. Then open `animation.gif` using your preferred program such as a web browser or file explorer.
