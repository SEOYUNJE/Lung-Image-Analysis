base_model = tfimm.create_model('cait_s24_224', in_channels=3, pretrained=False)

# PyTorch 모델에서 가중치 로드
pt_model = timm.create_model('cait_s24_224', pretrained=True)
pt_state_dict = pt_model.state_dict()

# TensorFlow 모델에 맞게 가중치 이름 변경
new_state_dict = {}
for name, weight in pt_state_dict.items():
    new_name = name.replace('/', '_')
    new_state_dict[new_name] = weight.numpy()

# TensorFlow 모델에 가중치 적용
for layer in base_model.layers:
    layer_name = layer.name.replace('_', '/')  # 원래 이름으로 변경

    if layer_name in new_state_dict:
        # 레이어의 가중치가 리스트 형태로 설정되어야 하므로
        layer.set_weights([new_state_dict[layer_name]])
