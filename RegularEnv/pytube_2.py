from pytube import YouTube
YouTube('https://youtu.be/PirsknaTofU?si=dqAC1D1vwXi9uevO').streams.first().download()