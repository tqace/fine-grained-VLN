name=speaker_data_balance_gap10
flag="--attn soft --angleFeatSize 128
      --train speaker
      --inst_gap 10
      --subout max --dropout 0.6 --optim adam --lr 1e-4 --iters 800000 --maxAction 35"
mkdir -p snap/$name
CUDA_VISIBLE_DEVICES=$1 python r2r_src/train.py $flag --name $name 

# Try this for file logging
# CUDA_VISIBLE_DEVICES=$1 unbuffer python r2r_src/train.py $flag --name $name | tee snap/$name/log
#--load snap/speaker/state_dict/best_val_unseen_bleu
