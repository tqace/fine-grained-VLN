name=agent_bt_fg
flag="--attn soft --train validlistener 
      --featdropout 0.3
      --submit
      --speaker snap/speaker/state_dict/best_val_unseen_bleu
      --load snap/agent_bt_fg/state_dict/best_val_unseen
      --angleFeatSize 128
      --feedback sample
      --mlWeight 0.2
      --subout max --dropout 0.5 --optim rms --lr 1e-4 --iters 80000 --maxAction 35"
mkdir -p snap/$name
CUDA_VISIBLE_DEVICES=$1 python r2r_src/train.py $flag --name $name 

# Try this with file logging:
# CUDA_VISIBLE_DEVICES=$1 unbuffer python r2r_src/train.py $flag --name $name | tee snap/$name/log
#flag="--attn soft --train validlistener 
#      --featdropout 0.3
#      --submit
#      --speaker snap/speaker/state_dict/best_val_unseen_bleu
#      --load snap/agent/state_dict/best_val_unseen
#      --angleFeatSize 128
#      --feedback sample
#      --mlWeight 0.2
#      --subout max --dropout 0.5 --optim rms --lr 1e-4 --iters 80000 --maxAction 35"
