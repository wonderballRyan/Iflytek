# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd#ipython notebook
adtrain = pd.read_csv(r"D:\3programme\we\competition1\round1_iflyad_train.txt",sep='\t')
# 指定分隔符。如果不指定参数，默认使用逗号分隔。如果分隔符长于一个字符并且不是‘\s+’，将使用python的语法分析器，并忽略数据中的逗号。正则表达式例子：'\r\t'
#adtrain.head(5)
#print (adtrain.describe())

adtrain.loc[adtrain["city"] == 0, "city"] = adtrain["city"].mode()[0]
# print (adtrain["city"].unique())
cityvar=adtrain["city"].unique()
i=0
for cityvar_num in cityvar:
    adtrain.loc[adtrain["city"] == cityvar[i], "city"] =i
    i=i+1
# print (adtrain["city"].unique())
    
adtrain.loc[adtrain["province"] == 0, "province"] = adtrain["province"].mode()[0]
provincevar=adtrain["province"].unique()
i=0
for provincevar_num in provincevar:
    adtrain.loc[adtrain["province"]==provincevar[i],"province"]=i
    i+=1
# print(adtrain["province"].unique())
    
advert_idvar=adtrain["advert_id"].unique()
i=0
for advert_idvar_num in advert_idvar:
    adtrain.loc[adtrain["advert_id"]==advert_idvar[i],"advert_id"]=i
    i+=1
# print(adtrain["province"].unique())

orderidvar=adtrain["orderid"].unique()
i=0
for orderid_num in orderidvar:
    adtrain.loc[adtrain["orderid"]==orderidvar[i],"orderid"]=i
    i+=1
#print(adtrain["orderid"].unique())

advert_industry_innervar=adtrain["advert_industry_inner"].unique()
i=0
for advert_industry_inner_num in advert_industry_innervar:
    adtrain.loc[adtrain["advert_industry_inner"]==advert_industry_innervar[i],"advert_industry_inner"]=i
    i+=1
#print(adtrain["advert_industry_inner"].unique())

campaign_idvar=adtrain["campaign_id"].unique()
i=0
for campaign_id_num in campaign_idvar:
    adtrain.loc[adtrain["campaign_id"]==campaign_idvar[i],"campaign_id"]=i
    i+=1
#print(adtrain["campaign_id"].unique())

creative_idvar=adtrain["creative_id"].unique()
i=0
for creative_id_num in creative_idvar:
    adtrain.loc[adtrain["creative_id"]==creative_idvar[i],"creative_id"]=i
    i+=1
#print(adtrain["creative_id"].unique())

creative_tp_dnfvar=adtrain["creative_tp_dnf"].unique()
i=0
for creative_tp_dnf_num in creative_tp_dnfvar:
    adtrain.loc[adtrain["creative_tp_dnf"]==creative_tp_dnfvar[i],"creative_tp_dnf"]=i
    i+=1
#print(adtrain["creative_tp_dnf"].unique())

#adtrain["app_cate_id"] = adtrain["app_cate_id"].fillna(adtrain["app_cate_id"].mode()[0])

app_idvar=adtrain["app_id"].unique()
i=0
for app_id_num in app_idvar:
    adtrain.loc[adtrain["app_id"]==app_idvar[i],"app_id"]=i
    i+=1
# print(adtrain["app_id"].unique())
    
inner_slot_idvar=adtrain["inner_slot_id"].unique()
i=0
for inner_slot_id_num in inner_slot_idvar:
    adtrain.loc[adtrain["inner_slot_id"]==inner_slot_idvar[i],"inner_slot_id"]=i
    i+=1
#print(adtrain["inner_slot_id"].unique())

adtrain.loc[adtrain["creative_is_jump"] == False, "creative_is_jump"] = 0
adtrain.loc[adtrain["creative_is_jump"] == True, "creative_is_jump"] = 1
# print(adtrain["creative_is_jump"].unique())

adtrain.loc[adtrain["creative_is_download"] == False, "creative_is_download"] = 0
adtrain.loc[adtrain["creative_is_download"] == True, "creative_is_download"] = 1
#print(adtrain["creative_is_jump"].unique())

adtrain.loc[adtrain["creative_is_voicead"] == False, "creative_is_voicead"] = 0
adtrain.loc[adtrain["creative_is_voicead"] == True, "creative_is_voicead"] = 1
# print(adtrain["creative_is_voicead"].unique())

adtrain.loc[adtrain["creative_is_js"] == False, "creative_is_js"] = 0
adtrain.loc[adtrain["creative_is_js"] == True, "creative_is_js"] = 1
#print(adtrain["creative_is_js"].unique())

adtrain.loc[adtrain["creative_has_deeplink"] == False, "creative_has_deeplink"] = 0
adtrain.loc[adtrain["creative_has_deeplink"] == True, "creative_has_deeplink"] = 1
#print(adtrain["creative_has_deeplink"].unique())

adtrain.loc[adtrain["app_paid"] == False, "app_paid"] = 0
adtrain.loc[adtrain["app_paid"] == True, "app_paid"] = 1
#print(adtrain["app_paid"].unique())

advert_namevar=adtrain["advert_name"].unique()
i=0
for advert_name_num in advert_namevar:
    adtrain.loc[adtrain["advert_name"]==advert_namevar[i],"advert_name"]=i
    i+=1
#print(adtrain["advert_name"].unique())

adidvar=adtrain["adid"].unique()
i=0
for adid_num in adidvar:
    adtrain.loc[adtrain["adid"]==adidvar[i],"adid"]=i
    i+=1
#print(adtrain["adid"].unique())
variables=["city","time","province","carrier","devtype","make","model","nnt","os","osv","os_name","adid","advert_id","orderid","advert_industry_inner","campaign_id","creative_id","creative_tp_dnf","app_cate_id","f_channel","app_id","inner_slot_id","creative_type","creative_width","creative_height","creative_is_jump","creative_is_download","creative_is_js","creative_is_voicead","creative_has_deeplink","app_paid","advert_name"]
for vari in variables:
    adtrain[vari] = adtrain[vari].fillna(adtrain[vari].mode()[0])
    
save = pd.DataFrame(adtrain) 
save.to_csv(r'D:\3programme\we\competition1\adtrain.csv')