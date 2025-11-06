import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd

    df = pd.read_csv('raw_training_study.csv')
    df
    return (df,)


@app.cell
def _(df):
    mask_gen = lambda d: d['hours'].notna() & d['score'].notna() & df['score'].between(0, 100)
    dropped_rows = df.loc[~mask_gen(df)]
    dropped_rows
    return (mask_gen,)


@app.cell
def _(df, mask_gen):
    clean_df = df.loc[mask_gen].drop(columns=['0'])
    clean_df.to_csv('study_data_clean.csv', index=False)

    clean_df
    return


if __name__ == "__main__":
    app.run()
