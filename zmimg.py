#
# Slice or build images for 2020 SFJS Yearbook Zoom screenshot images
#
# Written by Masa Hokari
# Started on 2020-12-28
#
# Notes:
# - Requires Python 3
# - Various parameters are fixed in this program.
# - See also the help message
#
# Screen size: W=3840 x H=2400
# Individual person image size: W=736 x H=414
# Gap between individual image: W=12, H=12
#
# Examples:
# python3 zmimg.py -a slice -i ~/Desktop/SFJS/Documents/test.png -o ~/Desktop/SFJS/Documents -l e5 -p "Student-" -q ".HOKA1234"
# python3 zmimg.py -a build -i "~/Desktop/SFJS/Documents/Student-\*.tif" -o ~/Desktop/SFJS/Documents/test2.png
#

import os
import glob
import getopt
import sys

from PIL import Image


def slice_image(dest_folder, src_file, config, prefix, postfix):
    x0, y0, dx, dy, gx, gy, nx, ny = config

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    image = Image.open(src_file)
    xi, yi = image.size
    num = 1
    y = y0
    for iy in range(ny):
        x = x0
        for ix in range(nx):
            box = (x, y, x + dx, y + dy)
            image2 = image.crop(box)
            output_file = os.path.join(dest_folder, "%s%02d%s.tif" % (prefix, num, postfix))
            if os.path.exists(output_file):
                raise Exception("File already exists: %s" % output_file)
            try:
                image2.save(output_file)
            except:
                pass
            num += 1
            x += dx + gx
        y += dy + gy


LAYOUT_CONFIG = (
    (0, 1),  # 0
    (1, 1),  # 1
    (2, 1),  # 2
    (3, 1),  # 3
    (2, 2),  # 4
    (3, 2),  # 5
    (3, 2),  # 6
    (3, 3),  # 7
    (3, 3),  # 8
    (3, 3),  # 9
    (4, 3),  # 10
    (4, 3),  # 11
    (4, 3),  # 12
    (4, 4),  # 13
    (4, 4),  # 14
    (4, 4),  # 15
    (4, 4),  # 16
    (4, 5),  # 17
    (4, 5),  # 18
    (4, 5),  # 19
    (4, 5),  # 20
    (5, 5),  # 21
    (5, 5),  # 22
    (5, 5),  # 23
    (5, 5),  # 24
    (5, 5),  # 25
)


def build_image(dest_file, src_files, config):
    (lx, ly, x0, y0, dx, dy, gx, gy, background_color) = config
    num_images = len(src_files)
    (ax, ay) = LAYOUT_CONFIG[num_images]
    a_total = ax * ay
    x0 += int((dx + gx) / 2 * (5 - ax))
    y0 += int((dy + gy) / 2 * (5 - ay))
    image_seq = 0
    py = y0
    collage = Image.new('RGB', (lx, ly), color=background_color)
    for iy in range(ay):
        px = x0
        num_images_not_pasted = num_images - image_seq
        is_last_row = num_images_not_pasted < ax
        if is_last_row:
            px += (dx + gx) / 2 * (ax - num_images_not_pasted)
        for ix in range(ax):
            image = Image.open(src_files[image_seq])
            box = image.getbbox()
            collage.paste(image, (int(px), int(py)))
            px += dx + gx
            image_seq += 1
            if image_seq >= num_images:
                break
        py += dy + gy
        if image_seq >= num_images:
            break

    try:
        collage.save(dest_file)
    except:
        pass


def main_slice(dest_folder, src_file, layout, prefix, postfix):
    print('Slicing image...')
    if True:
        # 3840 * 2000, macOS full screen
        x0 = 56
        y0 = 128
        dx = 736
        dy = 414
    elif False: # Mike's 3820 * 2400, 4 rows
        x0 = 46
        y0 = 354
        dx = 736
        dy = 414
    elif False: # Mike's 3820 * 2400, 5 rows, Variation 1
        x0 = 46
        y0 = 141
        dx = 736
        dy = 414
    elif False: # Mike's 3820 * 2400, 5 rows, Variation 2
        x0 = 56
        y0 = 567
        dx = 736
        dy = 414
    elif False: # Mike's 3820 * 2400, 5 rows, Variation 3
        x0 = 136
        y0 = 186
        dx = 704
        dy = 396
    elif False: # Mike's 3840 * 2400, 4 rows, Variation 1
        x0 = 136
        y0 = 390
        dx = 704
        dy = 396
    elif False: # Mike's 3840 * 2400, 4 rows, Variation 2
        x0 = 56
        y0 = 354
        dx = 736
        dy = 414
    elif False: # Mike's 3840 * 2400, 4 columns, 4 rows
        x0 = 110
        y0 = 432
        dx = 896
        dy = 503
    elif False:
        # 3840 * 2000, macOS full size window w/ BetterSnapTool
        x0 = 216
        y0 = 268
        dx = 672
        dy = 378
    elif False:
        # 3840 * 2000, macOS full size window w/ BetterSnapTool (2)
        x0 = 216
        y0 = 222
        dx = 672
        dy = 378
    else:
        # 6400 * 3600, macOS full screen
        x0 = 216
        y0 = 98
        dx = 1184
        dy = 666

    gx = 12
    gy = 12
    nx = 5
    ny = 5
    config_e5 = (x0, y0, dx, dy, gx, gy, nx, ny)
    x0 = x0 + (dx + gx) / 2
    nx = 4
    config_d5 = (x0, y0, dx, dy, gx, gy, nx, ny)
    
    # 3840 * 2000, macOS full screen
    x0 = 46
    y0 = 124
    dx = 928
    dy = 522

    gx = 12
    gy = 12
    nx = 4
    ny = 4
    config_d4 = (x0, y0, dx, dy, gx, gy, nx, ny)
    x0 = x0 + (dx + gx) / 2
    nx = 3
    config_c4 = (x0, y0, dx, dy, gx, gy, nx, ny)
    
    if layout == 'e5':
        config = config_e5
    elif layout == 'd5':
        config = config_d5
    elif layout == 'd4':
        config = config_d4
    elif layout == 'c4':
        config = config_c4
    else:
        print('ERROR: Unknown layout: %s' % layout)
        exit(1)
    slice_image(dest_folder, src_file, config, prefix, postfix)
    print(f'Done: {src_file}')


def main_build(dest_file, src_mask):
    print('Creating image...')
    lx = 3840
    ly = 2400
    x0 = 56
    y0 = 128
    dx = 736
    dy = 414
    gx = 12
    gy = 12
    background_color = (23, 23, 23)
    config = (lx, ly, x0, y0, dx, dy, gx, gy, background_color)
    src_files = []
    for file in glob.glob(src_mask):
        src_files.append(file)
    src_files.sort()
    build_image(dest_file, src_files, config)
    print(f'Done: {dest_file}')


def parse_arguments():
    SHORT_OPTIONS = 'ha:i:o:l:p:q:'
    LONG_OPTIONS = ['help', 'action=', 'input=', 'output=', 'layout=', 'prefix=', 'postfix=']
    opt_action = None
    opt_input = None
    opt_output = None
    opt_layout = 'e5'
    opt_prefix = 'Student'
    opt_postfix = ''

    argumentList = sys.argv[1:]
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, SHORT_OPTIONS, LONG_OPTIONS)

        # checking each argument
        for current_argument, current_value in arguments:

            if current_argument in ('-h', '--help'):
                print('python3 zmimg.py [-h] -a {action} -i {input} -o {output} [-l {layout}] [-p {prefix}] [-q {postfix}]')
                print('python3 zmimg.py -a slice -i {input_image_file} -o {output_folder} [-l {layout}] [-p {prefix}] [-q {postfix}]')
                print('python3 zmimg.py -a build -i {input_file_mask} -o {output_image_file}')
                print()
                print('\taction: \"slice\", \"build\"')
                print('\tinput: Input image file or image file mask')
                print('\toutput: Output image file or folder')
                print('\tlayout: \"e5\" (default), \"d5\", \"d4\", \"c4\"')
                print('\t\tRequired only for the slice action.')
                print('\tprefix: Any string, (default), \"Student-\"')
                print('\tpostfix: Any string, (default), \"\" (empty)')
                print()
                print('Notes:')
                print('\tIn the slice action, the sliced images are always saved as TIFF files'
                      ' and have file names \"Student-*.tif\".')
                print()
                print('Examples:')
                print('\t# Slice \"ClassPhoto1.png\" file and save the sliced TIFF images'
                      ' in \"Individuals\" folder.')
                print('\tpython3 zmimg.py -a slice -i ClassPhoto1.png -o Individuals -l e5 -p Student -q .HOKA1234')
                print()
                print('\t# Build an image from \"Individuals/Student-*.tif\" files and save as '
                      '\"ClassPhoto2.png\" file.')
                print('\tpython3 zmimg.py -a build -i "Individuals/Student-*.tif" -o ClassPhoto2.png')
                exit(0)

            elif current_argument in ('-a', '--action'):
                if current_value != 'slice' and current_value != 'build':
                    print('ERROR: Unknown action: %s' % current_value)
                    exit(1)
                opt_action = current_value

            elif current_argument in ('-i', '--input'):
                opt_input = os.path.expanduser(current_value)

            elif current_argument in ('-o', '--output'):
                opt_output = os.path.expanduser(current_value)

            elif current_argument in ('-l', '--layout'):
                if current_value != 'e5' and current_value != 'd5' and current_value != 'd4' and current_value != 'c4':
                    print('ERROR: Unknown layout: %s' % current_value)
                    exit(1)
                opt_layout = current_value

            elif current_argument in ('-p', '--prefix'):
                opt_prefix = current_value

            elif current_argument in ('-q', '--postfix'):
                opt_postfix = current_value

    except getopt.error as err:
        print(str(err))
        exit(1)

    if opt_action == None:
        print('Required argument missing: %s' % 'action')
        exit(1)
    if opt_input == None:
        print('Required argument missing: %s' % 'input')
        exit(1)
    if opt_output == None:
        print('Required argument missing: %s' % 'output')
        exit(1)

    return opt_action, opt_input, opt_output, opt_layout, opt_prefix, opt_postfix


def main():
    (opt_action, opt_input, opt_output, opt_layout, opt_prefix, opt_postfix) = parse_arguments()

    if opt_action == 'slice':
        main_slice(opt_output, opt_input, opt_layout, opt_prefix, opt_postfix)
    elif opt_action == 'build':
        main_build(opt_output, opt_input)
    else:
        print('ERROR: Unknown action: %s' % opt_action)
        exit(1)
    return 0


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("This program requires Python 3 or later.")
    main()
