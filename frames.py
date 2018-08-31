"""
Python3.6
python frames.py ./TARGET
対象ディレクトリ構造
./TARGET/発話者名/サンプル名/フレーム
"""
import os
import glob
import sys
import shutil

#各サンプルの最終フレームをコピーして最大フレームに統一
def copy_frame(dir_path, max_frames):
    #話者ディレクトリをListに取得
    speakers = glob.glob(dir_path+'/*')
    for sp in speakers:
        #サンプル名のListを取得
        samples = glob.glob(sp+'/*')
        for s in samples:
            print('sample_name:', s)
            files = glob.glob(s+'/*')
            n = len(files)
            f_title, f_ext = os.path.splitext(files[-1])
            for i in range(n, max_frames):
                shutil.copy(files[-1], s+'/{0:03d}'.format(i)+f_ext)

#アライメントの生成
def make_align(dir_path, max_frames):
    os.makedirs('align', exist_ok=True)
    #話者ディレクトリをListに取得
    speakers = glob.glob(dir_path+'/*')
    for sp in speakers:
        #サンプル名のListを取得
        samples = os.listdir(sp)
        for s in samples:
            sample_path = os.path.join(sp, s)
            f_title, f_ext = os.path.splitext(s)
            n = len(f_title)
            frames = os.listdir(sample_path)
            n_frames = len(frames)
            print(f_title)
            list = []
            list.append(0)
            list.append(n_frames * 1000)
            list.append(f_title[n-2:n])
            if n_frames < max_frames:
                list.append(n_frames * 1000)
                list.append(max_frames * 1000)
                list.append('sil')
            f = open('./align/'+f_title+'.align', 'a')
            count = 0
            for l in list:
                f.write(str(l))
                count +=1
                if count%3 == 0:
                    f.write('\n')
                else:
                    f.write(' ')
            f.close()

#最大フレーム数の取得
def count_max_frames(dir_path):
    #話者ディレクトリをListに取得
    speakers = glob.glob(dir_path+'/*')
    max_frames = 0
    for sp in speakers:
        #サンプル名のListを取得
        samples = os.listdir(sp)
        for s in samples:
            sample_path = os.path.join(sp, s)
            files = glob.glob(sample_path + '/*')
            if max_frames < len(files):
                max_frames = len(files)
    print('max_frames:',max_frames)
    return max_frames

def main():
    argv = sys.argv
    argl = len(argv)
    if (argl != 2):
        print('Usage: python ouluvs.py arg1')
        quit()
    else:
        max_frames = count_max_frames(argv[1])
        make_align(argv[1], max_frames)
        copy_frame(sys.argv[1], max_frames)

if __name__ == '__main__':
    main()