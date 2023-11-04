## 16. 🪐 流式星球

### 尝试与解决

> 关键词：二进制处理、枚举、手动解码

附件包含一个不能正常运行的 `create_video.py` 和一个 `video.bin`，其中 `create_video.py` 的功能似乎是录屏。看来，其作用只是告诉我们 `video.bin` 的格式。

关注生成 `video.bin` 的过程：

```python
    buffer = np.empty(shape=(frame_count, frame_height, frame_width, 3), dtype=np.uint8)

    for i in range(frame_count):
        success, frame = vidcap.read()
        if not success:
            raise Exception(f"Failed to read frame {i}")
        buffer[i] = frame

    buffer = buffer.reshape((frame_count * frame_height * frame_width, 3))
    buffer = buffer.ravel()
    buffer = buffer[:-random.randint(0, 100)]
    buffer.tofile(output)
```

这表明，`video.bin` 中每个三字节表示一个像素的颜色，按 RGB 方式编码，像素按行排列。但是，我们并不知道每帧的高度和宽度，并且由于 `buffer` 末端随机截除了一段，并不能通过文件大小的因数推断帧的尺寸。其中，宽度是关键，因为若宽度不对，图像会完全错位。

我们来写一个程序尝试解码：

```python
# 警告：此程序正常运行，会向文件系统内写入 800 张 png 图像

import os
from PIL import Image

output_path = 'video_stream_restore/output/'

if not os.path.exists(output_path):
    os.mkdir(output_path)

fp = open('./video_stream_restore/video.bin', 'rb')

frameWidth = 10
frameHeight = 1000
depth = 3

def dump_image_1():
    fp.seek(0, 0)
    stream = fp.read(frameWidth * frameHeight * depth)
    img = Image.frombytes('RGB', ( frameWidth, frameHeight ), stream)
    img.save(output_path + '1-' + str(frameWidth) + '.png')

for frameWidth in range(1, 800, 1):
    dump_image_1()
```

这个程序枚举了 1~800 的所有宽度并输出图像。用 Windows 照片查看器打开第一张，然后按住右方向键，这 800 张图像会快速滚动放映。此时集中注意力，可以发现宽度为 427 的图像具有非常完美的画面。

![](./assets/1-427.png)

*(为方便显示，这里旋转了图片方向)*

图像中间有明显的第一帧和第二帧的分界线。利用图像编辑器测量分界线的位置，可知帧高度是 759。接下来就可以通过程序解码所有帧。

```python
import os
from PIL import Image

output_path = 'video_stream_restore/output/'

if not os.path.exists(output_path):
    os.mkdir(output_path)

fp = open('./video_stream_restore/video.bin', 'rb')

frameWidth = 427
frameHeight = 759
depth = 3

t = 0
def dump_image_1():
    global t
    t += 1
    stream = fp.read(frameWidth * frameHeight * depth)
    img = Image.frombytes('RGB', ( frameWidth, frameHeight ), stream)
    img.save(output_path + 'frame-' + str(t) + '.png')

while True:
    dump_image_1()
```

最后这个程序会抛出 `Not enough data` 错误退出，表明解码完毕。观察比较靠后的帧可以看到上面有 flag 字幕。

![](./assets/frame-123.png)

### Flag

```plain
flag{it-could-be-easy-to-restore-video-with-haruhikage-even-without-metadata-0F7968CC}
```

It could be easy to restore video with haruhikage even without metadata.

haruhikage - 春日影？哦，是视频里的人物，那没事了。
