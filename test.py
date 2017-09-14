from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np

"""""
(rate,sig) = wav.read("sound_samples/test1.wav")


mfcc_feat= mfcc(sig,rate).T

print(mfcc_feat.shape)

mean_mfcc_feat=np.mean(mfcc_feat,1)
print(mean_mfcc_feat.shape)

cov_mfcc_feat=np.cov(mfcc_feat)

uppe_cov_mcc_feat=cov_mfcc_feat[np.triu_indices(13)]

feature_vector=np.concatenate((mean_mfcc_feat,uppe_cov_mcc_feat))
print(feature_vector.shape)

"""""
a=np.array([1,1,1,1,2,2,2,2])
b=np.array([2,1,1,2,2,1,1,1])
print(np.sum(a==b))