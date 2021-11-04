import csv
import re
import pandas as pd
import os
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import levene
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)
import time
import scikit_posthocs as sp
from scipy import stats
from scipy.stats import bartlett
Id_list = []
#### list space
### missing values
missing = []
##market price mean
Len_meanlist=[]
Min_meanlist=[]
Max_meanlist=[]
Mean_meanlist=[]
Q2_meanlist=[]
Q4_meanlist=[]
Q6_meanlist=[]
Q8_meanlist=[]

##store means
EP_meanlist=[]
EP_variance=[]
AP_meanlist=[]
AP_variance=[]
DM_meanlist=[]
DM_variance=[]
MP_meanlist=[]
MP_variance=[]
VS_meanlist=[]
VS_variance=[]
ZR_meanlist=[]
ZR_variance=[]

All_meanlist=[]
### Preishöhen
Low1p_meanlist=[]
Low2p_meanlist=[]
Midp_meanlist=[]
Highp_meanlist=[]
##Minimum Distence
EP_rmdlist=[]
AP_rmdlist=[]
DM_rmdlist=[]
MP_rmdlist=[]
VS_rmdlist=[]
ZR_rmdlist=[]
All_rmdlist=[]


### Quintiles

Q_EP =[]
Q_EPo =[]
Q_AP =[]
Q_APo =[]
Q_DM=[]
Q_DMo =[]
Q_MP =[]
Q_MPo =[]
Q_VS=[]
Q_VSo =[]
Q_ZR =[]
Q_ZRo =[]


### store mean rankings

EP_meanr =[]
AP_meanr =[]
DM_meanr =[]
MP_meanr =[]
VS_meanr =[]
ZR_meanr =[]

## defferentiation rate
diff_rate =[]



with open("C:/Users/Euronymus/Desktop/Scrapeyscrapey/selenium test/datasample_zurrose.csv", 'r') as file:
    reader = csv.reader(file)

    # ids into list and data frame creation
    list_ids_all = []
    for row in reader:
        entry = str(row)
        non_decimal = re.compile(r'[^\d.]+')
        p = non_decimal.sub('', entry)
        list_ids_all.append(p)

    print(list_ids_all)
    print(len(list_ids_all))
    file.close()

    #df = pd.DataFrame({"Id": list_ids_all})

    #print(len(df))
    #print(df)
allproducts = pd.read_excel('C:/Users/Euronymus/Desktop/Scrapeyscrapey/selenium test/Dataframes/Mindfactory/Zurrose/Dataframe_late_Zurrose.xlsx', index_col=0,
              dtype={'EAN': str,'Store': str})
              #na_values = [-9])

dataframe_all = pd.DataFrame(allproducts)

##start big loop
#
for EAN in list_ids_all:

        ##EAN
        Id_list.append(EAN)
        part = dataframe_all.loc[dataframe_all["EAN"] == EAN]

        #print(part)
        #print(EAN)
        #### Reduce to only stores ###

        new = part
            #.drop(part.index[[6, 7, 8, 9, 10, 11, 12,13]])
        #print(new)
        ## Compuland
        # Stores = ["CL", "CLC", "DC", "MF", "MFC", "VO"]
        ## Mean and CLeaning of stores
        try:
            Store = new.loc[new.Store == "EP"]

            store_list = []

            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
         #   print(store_list)

            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
          #  print(s_mean)
            mean_EP = float(sum(s_mean) / len(s_mean))

            # missing.append(len(s_missingv))
            EP_fail=[]
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                EP_fail.append("1")
                EP_meanlist.append("-9")
                EP_variance.append("-9")
            else:
                EP_meanlist.append(mean_EP)
                EP_variance.append(np.var(s_mean))
        except:
            EP_meanlist.append("-9")
            EP_variance.append("-9")
            s_fail.append("1")
        #print("CL")
        #print(mean_CL)
        store_list = []
        ###Compuland City
        try:
            Store = new.loc[new.Store == "AP"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
         #   print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
          #  print(s_mean)
            mean_AP = float(sum(s_mean) / len(s_mean))
            AP_fail=[]
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                AP_fail.append("1")
                AP_meanlist.append("-9")
                AP_variance.append("-9")
            else:
                AP_meanlist.append(mean_AP)
                AP_variance.append(np.var(s_mean))
           # print(CLC_meanlist)
        except:
            AP_meanlist.append("-9")
            AP_variance.append("-9")
            #mean_AP.append("-9")
            s_fail.append("1")
        store_list = []
        ###Drive City
        try:
            Store = new.loc[new.Store == "DM"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_DM = float(sum(s_mean) / len(s_mean))
            DM_fail=[]
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                DM_fail.append("1")
                DM_meanlist.append("-9")
                DM_variance.append("-9")
            else:
                DM_meanlist.append(mean_DM)
                DM_variance.append(np.var(s_mean))
        except:
            DM_meanlist.append("-9")
            DM_variance.append("-9")
            s_fail.append("1")
        store_list = []
        ###Mindfactory
        try:
            Store = new.loc[new.Store == "MP"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_MP = float(sum(s_mean) / len(s_mean))
            MP_fail=[]
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                MP_fail.append("1")
                MP_meanlist.append("-9")
                MP_variance.append("-9")
            else:
                MP_meanlist.append(mean_MP)
                MP_variance.append(np.var(s_mean))
        except:
            MP_meanlist.append("-9")
            MP_variance.append("-9")
            s_fail.append("1")
        store_list = []
        ###Mindfactory City
        try:
            Store = new.loc[new.Store == "VS"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_VS = float(sum(s_mean) / len(s_mean))
            VS_fail = []
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                VS_fail.append("1")
                VS_meanlist.append("-9")
                VS_variance.append("-9")
            else:
                VS_meanlist.append(mean_VS)
                VS_variance.append(np.var(s_mean))
            # print(s_mean)
            # print(s_missingv)
            # print(len(store_list))
            # print(len(s_missingv))
        except:
            VS_meanlist.append("-9")
            VS_variance.append("-9")
            s_fail.append("1")
        #print(MFC_meanlist)
        store_list = []
        ###Vibu Online
        try:
            Store = new.loc[new.Store == "ZR"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
        #    print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_ZR = float(sum(s_mean) / len(s_mean))
            ZR_fail = []
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                ZR_fail.append("1")
                ZR_meanlist.append("-9")
                ZR_variance.append("-9")
            else:
                ZR_meanlist.append(mean_ZR)
                ZR_variance.append(np.var(s_mean))
            #print(VO_meanlist)
        except:
            ZR_meanlist.append("-9")
            ZR_variance.append("-9")
            s_fail.append("1")
            ZR_fail.append("1")
            mean_ZR= "-9"
            #print(part)

        ###Mean all
        ### Fail Values rausnehmen

        if float(len(EP_fail))>0:
            mean_EP=float("-9")
        if float(len(AP_fail))>0:
            mean_AP=float("-9")
        if float(len(DM_fail))>0:
            mean_DM=float("-9")
        if float(len(MP_fail))>0:
            mean_MP=float("-9")
        if float(len(VS_fail))>0:
            mean_VS=float("-9")
        if float(len(ZR_fail))>0:
            mean_ZR=float("-9")


        means = [mean_EP, mean_AP, mean_DM, mean_MP, mean_VS, mean_ZR]
        fail=[]
        for mean in means:
            if float(mean)<0:
                fail.append("1")
                print("FAIL")
                print(fail)

        if float(mean_EP)<0:
            fail.append("1")
        if float(mean_AP)<0:
            fail.append("1")
        if float(mean_DM)<0:
            fail.append("1")
        if float(mean_MP)<0:
            fail.append("1")
        if float(mean_VS)<0:
            fail.append("1")
        if float(mean_ZR)==float("-9"):
            fail.append("1")

        if float(len(fail))>0:
            All_meanlist.append("-9")
            ### Preishöhen
            Low1p_meanlist.append("-9")
            Low2p_meanlist.append("-9")
            Midp_meanlist.append("-9")
            Highp_meanlist.append("-9")
        else:
            All_mean = float(sum(means))/float(len(means))
            All_meanlist.append(All_mean)
            if All_mean<10:
                Low1p_meanlist.append("1")
                Low2p_meanlist.append("0")
                Midp_meanlist.append("0")
                Highp_meanlist.append("0")
            if All_mean<30:
                if All_mean>10:
                    Low1p_meanlist.append("0")
                    Low2p_meanlist.append("1")
                    Midp_meanlist.append("0")
                    Highp_meanlist.append("0")
            if All_mean<100:
                if All_mean>30:
                    Low1p_meanlist.append("0")
                    Low2p_meanlist.append("0")
                    Midp_meanlist.append("1")
                    Highp_meanlist.append("0")
            if All_mean>100:
                Low1p_meanlist.append("0")
                Low2p_meanlist.append("0")
                Midp_meanlist.append("0")
                Highp_meanlist.append("1")

        #### Minimum distance
        #means = [mean_CL,mean_CLC,mean_DC,mean_MF,mean_MFC,mean_VO]
        #CL
        if float(len(fail))>0:
            EP_rmdlist.append("-9")
            AP_rmdlist.append("-9")
            DM_rmdlist.append("-9")
            MP_rmdlist.append("-9")
            VS_rmdlist.append("-9")
            ZR_rmdlist.append("-9")
        else:
            EP_rmd = (mean_EP/min(means))-1
            EP_rmdlist.append(EP_rmd)


            AP_rmd = (mean_AP/min(means))-1
            AP_rmdlist.append(AP_rmd)

            DM_rmd = (mean_DM / min(means)) - 1
            DM_rmdlist.append(DM_rmd)

            MP_rmd = (mean_MP / min(means)) - 1
            MP_rmdlist.append(MP_rmd)

            VS_rmd = (mean_VS / min(means)) - 1
            VS_rmdlist.append(VS_rmd)

            ZR_rmd = (mean_ZR / min(means)) - 1
            ZR_rmdlist.append(ZR_rmd)



        # Rmd all
        if float(len(fail))>0:
            All_rmdlist.append("-9")
        else:
            All_rmd = (EP_rmd + AP_rmd + DM_rmd + EP_rmd + VS_rmd + ZR_rmd) / 6
            All_rmdlist.append(All_rmd)


        #### Marktdate von Guenstiger.de


        new = part

        Store = new.loc[new.Store == "guen_len"]

        store_list = []

        for store in Store.iloc[0, :]:
            store_list.append(store)
        store_list.pop(0)
        store_list.pop(0)
        #print(store_list)
        #print("storelist")
        s_mean=[]
        s_missingv=[]
        s_fail=[]
        for s in store_list:
            if float(s) == float("-9"):
                s_missingv.append("1")
            else:
                s_mean.append(s)
            #print(s_mean)
        if len(s_mean)==0:
            mean_Len="-9"
        else:
            mean_Len = float(sum(s_mean)/len(s_mean))
            #print(mean_Len)
            #missing.append(len(s_missingv))

        if (float((len(store_list)) - float(len(s_missingv)))) < 20:
            s_fail.append("1")
            Len_meanlist.append("-9")
            Min_meanlist.append("-9")
            Max_meanlist.append("-9")
            Mean_meanlist.append("-9")
            Q2_meanlist.append("-9")
            Q4_meanlist.append("-9")
            Q6_meanlist.append("-9")
            Q8_meanlist.append("-9")
            #print("lenfail")
            #if float(mean_Len) < 5:
            #    Len_meanlist.append("-9")
            #    Min_meanlist.append("-9")
            #    Max_meanlist.append("-9")
            #    Mean_meanlist.append("-9")
            #    Q2_meanlist.append("-9")
            #    Q4_meanlist.append("-9")
            #    Q6_meanlist.append("-9")
            #    Q8_meanlist.append("-9")
            #    print("numberfaiil")

        else:

            Len_meanlist.append(mean_Len)

                ###Minimum

            Store = new.loc[new.Store == "guen_min"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            #print("market")
            #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
                #print(s_mean)
            mean_Min = float(sum(s_mean) / len(s_mean))
            #print("meanmin")

            Min_meanlist.append(mean_Min)
            #print(mean_Min)
                #print(Min_meanlist)
            store_list = []




            ###Maximum

            Store = new.loc[new.Store == "guen_max"]
            #print("store-max")
            #print(Store)
            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
                #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
                #print(s_mean)
            mean_Max = float(sum(s_mean) / len(s_mean))
            Max_meanlist.append(mean_Max)
            #print(mean_Max)
                #print(Max_meanlist)
            store_list = []

                ###Mean

            Store = new.loc[new.Store == "guen_mean"]
            #print("store-mean")
            #print(Store)
            store_list = []
            for s in Store.iloc[0, :]:
                store_list.append(s)
            store_list.pop(0)
            store_list.pop(0)
                #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                s_mean.append(s)
                #print(s_mean)
            mean_Mean = float(sum(s_mean) / len(s_mean))
            Mean_meanlist.append(mean_Mean)
            #print(mean_Mean)
                #print(Mean_meanlist)
            store_list = []

                ###0.2 Quantile

            Store = new.loc[new.Store == "guen_q_a"]
            #print("store-qa")
            #print(Store)
            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
                #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    pass
                else:
                    s_mean.append(s)
                #print(s_mean)
            mean_q2 = float(sum(s_mean) / len(s_mean))
            Q2_meanlist.append(mean_q2)
            #print("meanq2")
            #print(mean_q2)
            #print(Q2_meanlist)
            store_list = []

            ###0.4 Quantile

            Store = new.loc[new.Store == "guen_q_b"]
            #print("store-qb")
            #print(Store)
            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
                #print(s_mean)
            mean_q4 = float(sum(s_mean) / len(s_mean))
            Q4_meanlist.append(mean_q4)
            #print(mean_q4)
                #print(Q4_meanlist)
            store_list = []

                ###0.6 Quantile

            Store = new.loc[new.Store == "guen_q_c"]
           # print("store-qc")
            #print(Store)
            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
                #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
                #print(s_mean)
            mean_q6 = float(sum(s_mean) / len(s_mean))
            Q6_meanlist.append(mean_q6)
            #print(mean_q6)
                #print(Q6_meanlist)
            store_list = []

                ###0.8 Quantile

            Store = new.loc[new.Store == "guen_q_d"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
                #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
                #print(s_mean)
            mean_q8 = float(sum(s_mean) / len(s_mean))
            Q8_meanlist.append(mean_q8)
                #print(mean_q8)
                #print(Q8_meanlist)
            store_list = []

        #print(mean_Len)
        #print(asf)

        store_list = []

        ##### check market prices against quintiles

        if float(mean_Len)==float("-9"):
            Q_EP.append("-9")
            Q_EPo.append("-9")
            Q_AP.append("-9")
            Q_APo.append("-9")
            Q_DM.append("-9")
            Q_DMo.append("-9")
            Q_MP.append("-9")
            Q_MPo.append("-9")
            Q_VS.append("-9")
            Q_VSo.append("-9")
            Q_ZR.append("-9")
            Q_ZRo.append("-9")
        else:
            ### Quitiles CL
            #print("Mean_CL<meanmin")
            #print(mean_CL)
            if float(mean_EP)==float("-9"):
                Q_EP.append("-9")
                Q_EPo.append("-9")
            else:
                if float(mean_EP)<=mean_Min:
                    Q_EP.append("0")
                    Q_EPo.append("0")
                    print(Q_EP)

                if float(mean_EP) <= mean_q2:
                    if float(mean_EP) > mean_Min:
                        Q_EP.append("0,1")
                        Q_EPo.append("1")

                if float(mean_EP) <= mean_q4:
                    if float(mean_EP) > mean_q2:
                        Q_EP.append("0,3")
                        Q_EPo.append("2")

                if float(mean_EP) <= mean_q6:
                    if float(mean_EP) > mean_q4:
                        Q_EP.append("0,5")
                        Q_EPo.append("3")

                if float(mean_EP) <= mean_q8:
                    if float(mean_EP) > mean_q6:
                        Q_EP.append("0,7")
                        Q_EPo.append("4")

                if float(mean_EP) <= mean_Max:
                    if float(mean_EP) > mean_q8:
                        Q_EP.append("0,9")
                        Q_EPo.append("5")

                if float(mean_EP) > mean_Max:
                    Q_EP.append("1")
                    Q_EPo.append("6")
                print(Q_EP)
                ### Quitiles CLC
            if float(mean_AP)==float("-9"):
                Q_AP.append("-9")
                Q_APo.append("-9")
            else:
                if float(mean_AP) <= mean_Min:
                    Q_AP.append("0")
                    Q_APo.append("0")

                if float(mean_AP) <= mean_q2:
                    if float(mean_AP) > mean_Min:
                        Q_AP.append("0,1")
                        Q_APo.append("1")

                if float(mean_AP) <= mean_q4:
                    if float(mean_AP) > mean_q2:
                        Q_AP.append("0,3")
                        Q_APo.append("2")

                if float(mean_AP) <= mean_q6:
                    if float(mean_AP) > mean_q4:
                        Q_AP.append("0,5")
                        Q_APo.append("3")

                if float(mean_AP) <= mean_q8:
                    if float(mean_AP) > mean_q6:
                        Q_AP.append("0,7")
                        Q_APo.append("4")

                if float(mean_AP) <= mean_Max:
                    if float(mean_AP) > mean_q8:
                        Q_AP.append("0,9")
                        Q_APo.append("5")

                if float(mean_AP) > mean_Max:
                    Q_AP.append("1")
                    Q_APo.append("6")
                print(Q_AP)
                ###DM
                #####'''''''
            if float(mean_DM) < 0:
                Q_DM.append("-9")
                Q_DMo.append("-9")
            else:
                ### Quitiles AP

                if float(mean_DM) <= mean_Min:
                    Q_DM.append("0")
                    Q_DMo.append("0")

                if float(mean_DM) <= mean_q2:
                    if float(mean_DM) > mean_Min:
                        Q_DM.append("0,1")
                        Q_DMo.append("1")

                if float(mean_DM) <= mean_q4:
                    if float(mean_DM) > mean_q2:
                        Q_DM.append("0,3")
                        Q_DMo.append("2")

                if float(mean_DM) <= mean_q6:
                    if float(mean_DM) > mean_q4:
                        Q_DM.append("0,5")
                        Q_DMo.append("3")

                if float(mean_DM) <= mean_q8:
                    if float(mean_DM) > mean_q6:
                        Q_DM.append("0,7")
                        Q_DMo.append("4")

                if float(mean_DM) <= mean_Max:
                    if float(mean_DM) > mean_q8:
                        Q_DM.append("0,9")
                        Q_DMo.append("5")

                if float(mean_DM) > mean_Max:
                    Q_DM.append("1")
                    Q_DMo.append("6")

                print(Q_DM)

            ### Quitiles MF
            if float(mean_MP) < 0:
                Q_MP.append("-9")
                Q_MPo.append("-9")
            else:

                if float(mean_MP) <= mean_Min:
                    Q_MP.append("0")
                    Q_MPo.append("0")

                if float(mean_MP) <= mean_q2:
                    if mean_MP > mean_Min:
                        Q_MP.append("0,1")
                        Q_MPo.append("1")

                if float(mean_MP) <= mean_q4:
                    if float(mean_MP) > mean_q2:
                        Q_MP.append("0,3")
                        Q_MPo.append("2")

                if float(mean_MP) <= mean_q6:
                    if float(mean_MP) > mean_q4:
                        Q_MP.append("0,5")
                        Q_MPo.append("3")

                if float(mean_MP) <= mean_q8:
                    if float(mean_MP) > mean_q6:
                        Q_MP.append("0,7")
                        Q_MPo.append("4")

                if float(mean_MP) <= mean_Max:
                    if float(mean_MP) > mean_q8:
                        Q_MP.append("0,9")
                        Q_MPo.append("5")

                if float(mean_MP) > mean_Max:
                    Q_MP.append("1")
                    Q_MPo.append("6")

#######################################################
            #EQ=[]
            if float(mean_ZR) == float("-9"):
                #Succ.append("1")
                Q_ZR.append("-9")
                Q_ZRo.append("-9")

            #if float(mean_Min) or float(mean_Max) or float(mean_q2) or float(mean_q4) or float(mean_q8) == float(mean_ZR):
             #   Q_ZR.append("-9")
              #  Q_ZRo.append("-9")

            else:
                ### Quitiles ZR

                if float(mean_ZR) <= float(mean_Min):
                    Q_ZR.append("0")
                    Q_ZRo.append("0")

                if float(mean_ZR) <= float(mean_q2):
                    if float(mean_ZR) > float(mean_Min):
                        Q_ZR.append("0,1")
                        Q_ZRo.append("1")
            #            Succ.append("1")
                if float(mean_ZR) <= float(mean_q4):
                    if float(mean_ZR) > float(mean_q2):
                        Q_ZR.append("0,3")
                        Q_ZRo.append("2")
            #            Succ.append("1")

                if float(mean_ZR) <= float(mean_q6):
                    if float(mean_ZR) > float(mean_q4):
                        Q_ZR.append("0,5")
                        Q_ZRo.append("3")
            #            Succ.append("1")

                if float(mean_ZR) <= float(mean_q8):
                    if float(mean_ZR) > float(mean_q6):
                        Q_ZR.append("0,7")
                        Q_ZRo.append("4")
            #            Succ.append("1")

                if float(mean_ZR) <= float(mean_Max):
                    if float(mean_ZR) > float(mean_q8):
                        Q_ZR.append("0,9")
                        Q_ZRo.append("5")
            #            Succ.append("1")

                if float(mean_ZR) > float(mean_Max):
                    Q_ZR.append("1")
                    Q_ZRo.append("6")
            #        Succ.append("1")



            #if len(Succ)<1:
            #    Q_ZR.append("-9")
            #    Q_ZRo.append("-9")

            ### Quitiles VS

            if float(mean_VS) == float("-9"):

                Q_VS.append("-9")
                Q_VSo.append("-9")
            else:
                if float(mean_VS) <= float(mean_Min):
                    Q_VS.append("0")
                    Q_VSo.append("0")

                if float(mean_VS) <= float(mean_q2):
                    if float(mean_VS) > float(mean_Min):
                        Q_VS.append("0,1")
                        Q_VSo.append("1")

                if float(mean_VS) <= float(mean_q4):
                    if float(mean_VS) > float(mean_q2):
                        Q_VS.append("0,3")
                        Q_VSo.append("2")

                if float(mean_VS) <= float(mean_q6):
                    if float(mean_VS) > float(mean_q4):
                        Q_VS.append("0,5")
                        Q_VSo.append("3")

                if float(mean_VS) <= float(mean_q8):
                    if float(mean_VS) > float(mean_q6):
                        Q_VS.append("0,7")
                        Q_VSo.append("4")

                if float(mean_VS) <= float(mean_Max):
                    if float(mean_VS) > float(mean_q8):
                        Q_VS.append("0,9")
                        Q_VSo.append("5")

                if float(mean_VS) > float(mean_Max):
                    Q_VS.append("1")
                    Q_VSo.append("6")

        ###store means ranks
        new = part.drop(part.index[[6, 7, 8, 9, 10, 11, 12, 13]])
        #print(Store)
        base = new.iloc[:, 0]

        #print(base)

        base_list = []

        #print(base_list)
        ## data for parametric test
        add_list = []
        ### data for non parametric test

        ranking_stores = ["r_EP", "r_AP","r_DM","r_MP", "r_VS","r_ZR"]
        df_ranking = pd.DataFrame(ranking_stores)

        ## Ranking lists

        r_EP = []
        r_AP = []
        r_DM = []
        r_MP = []
        r_VS = []
        r_ZR = []


        no_diff =[]
        yes_diff=[]

        for b in range(3, 53):
            addon = new.iloc[:, int(b)]

            part_list = []
            fail_list = []

            ## check for missing values
            for c in addon:
                if float(c) == float("-9"):
                    fail_list.append("1")
#
                else:
                    pass
#
            if len(fail_list)>0:
                pass

            ### ranking Price data
            else:
                np_list = []
                s = pd.Series(addon)
                q = s.rank(method='dense')
                for s in q:
                    np_list.append(s)

                #print(np_list)


            ###check for no differentiation

                if np_list[0]==np_list[1]==np_list[2]==np_list[3]==np_list[4]==np_list[5]:
                    no_diff.append("1")
                else:
                    yes_diff.append("1")

                r_EP.append(np_list[0])
                r_AP.append(np_list[1])
                r_DM.append(np_list[2])
                r_MP.append(np_list[3])
                r_VS.append(np_list[4])
                r_ZR.append(np_list[5])

                #print(r_CL)
                #print(r_CLC)
                #print(r_MF)




        if len(r_EP) < 20:
            EP_meanr.append("-9")
            AP_meanr.append("-9")
            DM_meanr.append("-9")
            MP_meanr.append("-9")
            VS_meanr.append("-9")
            ZR_meanr.append("-9")
            diff_rate.append("-9")
        else:
            EP_meanr.append(sum(r_EP)/len(r_EP))
            AP_meanr.append(sum(r_AP)/len(r_AP))
            DM_meanr.append(sum(r_DM)/len(r_DM))
            MP_meanr.append(sum(r_MP)/len(r_MP))
            VS_meanr.append(sum(r_VS)/len(r_VS))
            ZR_meanr.append(sum(r_ZR)/len(r_ZR))
            #print(len(yes_diff))
            #print(len(r_CL))
            diff_rate.append(len(yes_diff)/len(r_EP))




print(len(Id_list))
print(len(EP_meanlist))
print(len(AP_meanlist))
print(len(DM_meanlist))
print(len(MP_meanlist))
print(len(VS_meanlist))
print(len(ZR_meanlist))

print(len(Len_meanlist))
print(Len_meanlist)
print(len(Min_meanlist))
print(Min_meanlist)
print(len(Max_meanlist))
#ürint(Max_meanlist)
print(len(Q2_meanlist))
print(Q2_meanlist)
print(len(Q4_meanlist))
print(Q4_meanlist)
print(len(Q6_meanlist))
print(Q6_meanlist)
print(len(Q8_meanlist))
print(Q8_meanlist)

print(len(Q_EP))
print(len(Q_EPo))
print(len(Q_AP))
print(len(Q_APo))
print(len(Q_DM))
print(len(Q_DMo))
print(len(Q_MP))
print(len(Q_MPo))
print(len(Q_VS))
print(len(Q_VSo))
print(len(Q_ZR))
print(len(Q_ZRo))
print(Q_ZRo)
dfend = pd.DataFrame({'EAN': Id_list, "mean_EP":EP_meanlist,"var_EP":EP_variance,"mean_AP":AP_meanlist,"var_AP":AP_variance,
                      "mean_DM":DM_meanlist,"var_DM":DM_variance,"mean_MP":MP_meanlist,"var_MP":MP_variance, "mean_VS":VS_meanlist,"var_VS":VS_variance, "mean_ZR":ZR_meanlist, "var_ZR":ZR_variance,
                       "meanr_EP":EP_meanr,"meanr_AP":AP_meanr,"meanr_DM":DM_meanr,"meanr_MP":MP_meanr,"meanr_VS":VS_meanr,"meanr_ZR":ZR_meanr,"diff_rate":diff_rate,
                      "All_rmd":All_rmdlist, "EP_rmd":EP_rmdlist,"AP_rmd":AP_rmdlist,"DM_rmd":DM_rmdlist,"MP_rmd":MP_rmdlist,"VS_rmd":VS_rmdlist,"ZR_rmd":ZR_rmdlist,
                      "All_mean":All_meanlist,"Low1p":Low1p_meanlist,"Low2p":Low2p_meanlist,"Midp":Midp_meanlist,"Highp":Highp_meanlist,
                      "Len_mp":Len_meanlist, "Min_mp":Min_meanlist, "Max_mp":Max_meanlist, "Mean_mp":Mean_meanlist, "Q2_mp":Q2_meanlist,"Q4_mp":Q4_meanlist,"Q6_mp":Q6_meanlist,"Q8_mp":Q8_meanlist,
                      "Q_EP":Q_EP,"Q_EPo":Q_EPo, "Q_AP":Q_AP, "Q_APo":Q_APo,"Q_DM":Q_DM,"Q_DMo":Q_DMo,"Q_MP":Q_MP, "Q_MPo":Q_MPo, "Q_VS":Q_VS, "Q_VSo":Q_VSo, "Q_ZR":Q_ZR, "Q_ZRo":Q_ZRo,
                     })

dfend.to_excel('DF_VSCleaning_late.xlsx')