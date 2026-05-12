import os
import shutil
from datetime import datetime

obsidian_Url = "/Users/songxinbi/Desktop/test/a"
target_Url = "/Users/songxinbi/Desktop/test/b"


def sync_ob_tar(obsi_url, targ_url):

    add_num, cover_num, skip_num = 0, 0, 0
    for root, dirs, files in os.walk(obsi_url):
        """
        root:当前文件夹的完整路径
        dirs:当前文件夹下的文件夹
        files:当前文件夹下的文件
        """
        if "模板" in dirs:
            dirs.remove("模板")
        rel_path = os.path.relpath(root, obsi_url)
        target_dir = os.path.join(targ_url, rel_path)
        os.makedirs(target_dir, exist_ok=True)

        for file in files:
            # 获取当前源文件和目标文件的地址
            src_file = os.path.join(root,file)
            dst_file = os.path.join(target_dir, file)

            # 获取当前源文件的时间戳
            src_mtime = os.path.getmtime(src_file)
            src_time = datetime.fromtimestamp(src_mtime).strftime("%Y-%m-%d %H:%M:%S")

            # 核心同步逻辑
            # 如果目标文件不存在，则复制源文件到目标文件
            if not os.path.exists(dst_file):
                shutil.copy2(src_file, dst_file)
                print(f"新增{file}{src_time}")
                add_num += 1

            # 如果目标文件存在，则比较源文件和目标文件的时间戳
            else:
                dst_mtime = os.path.getmtime(dst_file)
                if src_mtime > dst_mtime:
                    shutil.copy2(src_file, dst_file)
                    print(f"覆盖{file}{src_time}")
                    cover_num += 1

                else:
                    print(f"跳过{file}{src_time}")
                    skip_num += 1
    print(f"新增{add_num}个，覆盖{cover_num}个，跳过{skip_num}个")

if __name__ == "__main__":
    print("开始同步。。。。")
    sync_ob_tar(obsidian_Url, target_Url)
    print("完成结束。。。。")