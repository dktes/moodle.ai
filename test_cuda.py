import torch
cuda_avail = torch.cuda.is_available()

if cuda_avail:
	print("cuda availabe:- ",)
	print("Current device:- ",torch.cuda.current_device())
	print("DEVICE NAME:- ",torch.cuda.get_device_name(torch.cuda.current_device()))
	print("CUDNN VERSION:- ",torch.backends.cudnn.version())
	
else:
	print("Cuda not available...")
