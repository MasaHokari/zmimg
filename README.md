zmimg

Image slicer and builder for 2020 SFJS Yearbook Zoom screenshot

# Installation

1. Install Python3 if you don't have yet
1. Get source code
   - `git clone https://github.com/MasaHokari/zmimg`

# Commandline options

```shell
python3 zmimg.py [-h] -a {action} -i {input} -o {output} [-l {layout}]
```

- Commandline options
  - `action`: `slice`, `build`
  - `input`: Input image file or image file mask
  - `output`: Output image file or folder
  - `layout`: `e5` (default), `d5`
    - Required only for the slice action.

# Retouch workflow 
  1. Run `zmimg` command with `slice` action to slice a screenshot image and save individual portrait images.
    ```shell
    python3 zmimg.py -a slice -i {input_image_file} -o {output_folder} [-l {layout}]
    ```
  1. Retouch the individual portrait images and save them as new image files
     - Note that this program does not honor retouches done by Adobe CameraRaw directly.
      New image files need to be exported and use them in the next step.
  1. Run `zmimg` command with `build` action to build collage image from individual portrait images.
    ```shell
    python3 zmimg.py -a build -i {input_file_mask} -o {output_image_file}
    ```


# Notes
- In the slice action, the sliced images are always saved as TIFF files and have file names `Student-*.tif`.
- Requires Python 3
- Various parameters are fixed in this program.
    - Screen size: W=3840 x H=2400
    - Individual person image size: W=736 x H=414
    - Gap between individual image: W=12, H=12

# Examples
- Slice `ClassPhoto1.png` file and save the sliced TIFF images in `Individuals` folder. 

  ```shell
  python3 zmimg.py -a slice -i ClassPhoto1.png -o Individuals -l e5
  ```

- Build an image from `Individuals/Student-*.png` files and save as `ClassPhoto2.png` file.

  ```shell
  python3 zmimg.py -a build -i "Individuals/Student-*.png" -o ClassPhoto2.png
  ```
