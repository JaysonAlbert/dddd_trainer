import ddddocr
import shutil

det = ddddocr.DdddOcr(show_ad = False, import_onnx_path = './projects/piaoxingqiu/models/effnetv2_m_3/piaoxingqiu_1.0_3552_159000_2024-04-01-08-46-36.onnx',
                      charsets_path = './projects/piaoxingqiu/models/effnetv2_m_3/charsets.json',)

# for i in range(1500, 1510):
#     with open(f'./projects/piaoxingqiu/datasets_o/images/{i}.png', 'rb') as f:
#         image_bytes = f.read()

#     print(det.classification(image_bytes))

# print('\n\n')


for i in range(3600, 3630):
    with open(f'./projects/piaoxingqiu/datasets/images/{i}.png', 'rb') as f:
        image_bytes = f.read()
        
    shutil.copy(f'./projects/piaoxingqiu/datasets/images/{i}.png', f'./eval/{i}.png')

    print(det.classification(image_bytes))

print('\n\n')
