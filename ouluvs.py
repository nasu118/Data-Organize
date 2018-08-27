"""
Python3.6
python ouluvs.py ./OuluVS/images/P001_ROI ./TARGET/Ouluvs/P001
#テスト用
python ouluvs.py ./images/P001_ROI ./TARGET
分類対象の命名規則
P001_01_01_001_ROI_color.bmp
発話者名_サンプル名_発話内容番号_フレーム番号_ROI_（color or gray）
"""
import glob
import shutil
import sys
import os
import os.path

#対象のディレクトリ内のファイルをサンプルごとに分類してコピー
def file_copy(dir_path, new_dir_path):
    #ディレクトリ内のcolor画像のファイル名を取得
    files = os.listdir(dir_path)
    color = [f for f in files if 'color' in f]
    for f in color:
        num = f.find('_')
        sample_path = os.path.join(new_dir_path, f[num+1:num+6])
        color_path = os.path.join(dir_path, f)
        os.makedirs(sample_path, exist_ok=True)
        shutil.copy(color_path, sample_path)
    print('copy fin')

#リネーム処理
def rename(new_dir_path):
    samples = os.listdir(new_dir_path)
    for s in samples:
        samples_path = os.path.join(new_dir_path, s)
        files = os.listdir(samples_path)
        for i, f in enumerate(files):
            f_title, f_ext = os.path.splitext(f)
            os.rename(os.path.join(samples_path, f), os.path.join(samples_path, '{0:03d}'.format(i) + f_ext))
    print('rename fin')

def main():
    argv = sys.argv
    argl = len(argv)
    if (argl != 3):
        print('Usage: python ouluvs.py arg1 arg2')
        quit()
    else:
        os.makedirs(argv[2], exist_ok=True)
        file_copy(argv[1], argv[2])
        rename(argv[2])



if __name__ == '__main__':
    main()