import json

def load_model(args):
    if 'vlmevalkit_' in args.model_type: 
        from vlmevalkit_model_api import VLMEvalModel
        model = VLMEvalModel(model_type=args.model_type)
    else:
        raise NotImplementedError(f'{args.model_type} is not supported!')

    return model
