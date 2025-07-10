import os
import shutil

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches


class PPTXOperatorService:
    def __init__(self, pptx_file_name, output_base_path):
        self.pptx_file_name = pptx_file_name
        self.output_base_path = output_base_path

    def create_image(self, image_file_path):
        # 元ファイル(pptx)をコピー
        new_pptx_file_path = os.path.join(self.output_base_path, "output.pptx")
        shutil.copy(self.pptx_file_name, new_pptx_file_path)

        # pptxファイルを読み込む
        presentation = Presentation(new_pptx_file_path)

        # 最初のスライド取得
        slide = presentation.slides[0]

        # スライドサイズを取得して全体にフィット
        slide_width = presentation.slide_width
        slide_height = presentation.slide_height

        # 画像をスライドに追加（最背面にするには最初に追加）
        slide.shapes.add_picture(
            image_file_path, 0, 0, width=slide_width, height=slide_height
        )

        # PPTX保存
        presentation.save(new_pptx_file_path)

        return ""
