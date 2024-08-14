import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri

# sess = sagemaker.Session()
# sagemaker_session_bucket=None
# if sagemaker_session_bucket is None and sess is not None:
#     sagemaker_session_bucket = sess.default_bucket()

iam = boto3.client('iam')
role = iam.get_role(RoleName='AmazonSageMaker-ExecutionRole-20240814T155706')['Role']['Arn']

hub = {
	'HF_MODEL_ID':'meta-llama/Meta-Llama-3.1-8B',
	'SM_NUM_GPUS': json.dumps(1),
	'HUGGING_FACE_HUB_TOKEN': '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'
}
# import ipdb;ipdb.set_trace()
print(hub)

# sess = sagemaker.Session(default_bucket=sagemaker_session_bucket)
# print(sess.boto_region_name)
img = "763104351884.dkr.ecr.eu-north-1.amazonaws.com/huggingface-pytorch-tgi-inference:2.1.1-tgi2.0.0-gpu-py310-cu121-ubuntu22.04"
# img = "763104351884.dkr.ecr.eu-north-1.amazonaws.com/huggingface-pytorch-tgi-inference:2.1.1-tgi2.0.0-gpu-py310-cu121-ubuntu22.04"
# image_uri = "763104351884.dkr.ecr.{sess.boto_region_name}.amazonaws.com/huggingface-pytorch-tgi-inference:2.1-tgi2.0-gpu-py310-cu121-ubuntu22.04"
# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	image_uri=img,
	env=hub,
	role=role, 
)
# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1,
	instance_type="ml.g5.2xlarge",
	container_startup_health_check_timeout=300,
  )
  
# send request
predictor.predict({
	"inputs": "My name is Julien and I like to",
})