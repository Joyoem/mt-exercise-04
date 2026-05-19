#!/bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data
configs=$base/configs
translations=$base/translations

# best model
model_name="bpe_4000_en-ro"
orig_config="$configs/$model_name.yaml"
tmp_config="$configs/tmp_beam_experiment.yaml"

mkdir -p $translations/beam_search

num_threads=4
device=0

for k in {1..10}; do
    echo "----------------------------------------"
    echo "[$(date +%T)] processing Beam Size = $k ..."

    cp $orig_config $tmp_config

    sed -i '' "s/beam_size:.*/beam_size: $k/g" $tmp_config 2>/dev/null || sed -i "s/beam_size:.*/beam_size: $k/g" $tmp_config
    
    START_TIME=$SECONDS

    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python -m joeynmt translate \
        $tmp_config < $data/test.en > $translations/beam_search/test.beam$k.ro

    ELAPSED=$((SECONDS - START_TIME))

    BLEU_SCORE=$(sacrebleu $data/test.ro < $translations/beam_search/test.beam$k.ro -b)
    echo "[$(date +%T)] Beam $k finished! BLEU: $BLEU_SCORE costs: $ELAPSED seconds"
done

rm -f $tmp_config
