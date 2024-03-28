import ddddocr

det = ddddocr.DdddOcr(show_ad = False, import_onnx_path = './projects/piaoxingqiu/models/effnetv2_m_3/piaoxingqiu_0.96875_1176_65000_2024-03-28-14-29-37.onnx',
                      charsets_path = './projects/piaoxingqiu/models/effnetv2_m_3/charsets.json',)

for i in range(1500, 1510):
    with open(f'./projects/piaoxingqiu/datasets_o/images/{i}.png', 'rb') as f:
        image_bytes = f.read()

    print(det.classification(image_bytes))

print('\n\n')


for i in range(1500, 1510):
    with open(f'./projects/piaoxingqiu/datasets/images/{i}.png', 'rb') as f:
        image_bytes = f.read()

    print(det.classification(image_bytes))

print('\n\n')
