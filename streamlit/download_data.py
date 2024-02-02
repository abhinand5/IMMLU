from datasets import load_dataset

#Returns a Pandas DataFrame with the MMLU dataset
def return_df():

    #https://huggingface.co/datasets/lighteval/mmlu
    dataset = load_dataset('lighteval/mmlu', 'all', split = 'auxiliary_train')
    df_mmlu = dataset.to_pandas()
    return df_mmlu