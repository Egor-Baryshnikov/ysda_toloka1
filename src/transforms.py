from torchvision import transforms

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Resize((50, 200)), # Hint: this might not be the best way to resize images
     transforms.RandomAffine(30, (0.1,0.1), (0.9, 1.1)),
     transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) # Hint: this might not be the best normalization
     ]
)
