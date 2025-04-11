import pandas as pd
df1 = pd.read_excel("1.Manufac Estimation.xlsx",sheet_name="manufac_to_csv")
df2 = pd.read_excel("1.Manufac Estimation.xlsx",sheet_name="complete_to_csv")
df3 = pd.read_excel("1.Manufac Estimation.xlsx",sheet_name="wip_to_csv")
df1["EYM_YearMonth"] = df1['EYM_YearMonth'].astype("str")
df2["PD_YM"] = df2["PD_YM"].astype("str")
df3["IVT_YM"] = df3["IVT_YM"].astype("str")


df3 = pd.lreshape(df3,{"columname":["IVT_WIP","IVT_WIP_Previous","IVT_WIPCurrent","IVT_WIP_Cost_Difference"]})

[print(d) for d in [df1,df2,df3]]