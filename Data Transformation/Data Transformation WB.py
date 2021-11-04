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
BU_meanlist=[]
BU_variance=[]
JO_meanlist=[]
JO_variance=[]
WB_meanlist=[]
WB_variance=[]


All_meanlist=[]
### Preishöhen
Low1p_meanlist=[]
Low2p_meanlist=[]
Midp_meanlist=[]
Highp_meanlist=[]
##Minimum Distence
BU_rmdlist=[]
JO_rmdlist=[]
WB_rmdlist=[]

All_rmdlist=[]


### Quintiles

Q_BU =[]
Q_BUo =[]
Q_JO =[]
Q_JOo =[]
Q_WB=[]
Q_WBo =[]


### store mean rankings

BU_meanr =[]
JO_meanr =[]
WB_meanr =[]

## defferentiation rate
diff_rate =[]



with open("C:/Users/Euronymus/Desktop/Scrapeyscrapey/selenium test/datasample_weltbild_thalia.csv", 'r') as file:
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
allproducts = pd.read_excel('C:/Users/Euronymus/Desktop/Scrapeyscrapey/selenium test/Dataframes/Mindfactory/Weltbild/Dataframe_late_Weltbild.xlsx', index_col=0,
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
        print(new)
            #.drop(part.index[[6, 7, 8, 9, 10, 11, 12,13]])
        #print(new)
        ## Compuland
        # Stores = ["CL", "CLC", "DC", "MF", "MFC", "VO"]
        ## Mean and CLeaning of stores
        try:
            Store = new.loc[new.Store == "BU"]

            store_list = []

            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
         #   print(store_list)
            BU_fail = []
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
          #  print(s_mean)
            if float(len(s_mean))==0:
                BU_fail.append("1")
                BU_meanlist.append("-9")
                BU_variance.append("-9")
            else:
                mean_BU = float(sum(s_mean) / len(s_mean))

                # missing.append(len(s_missingv))

                if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                    BU_fail.append("1")
                    BU_meanlist.append("-9")
                    BU_variance.append("-9")
                else:
                    BU_meanlist.append(mean_BU)
                    BU_variance.append(np.var(s_mean))
        except:
            BU_meanlist.append("-9")
            BU_variance.append("-9")
            s_fail.append("1")
        #print("CL")
        #print(mean_CL)
        store_list = []
        ###Compuland City
        try:
            Store = new.loc[new.Store == "JO"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
         #   print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            JO_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
          #  print(s_mean)
            if float(len(s_mean))==0:
                JO_fail.append("1")
                JO_meanlist.append("-9")
                JO_variance.append("-9")
            else:
                mean_JO = float(sum(s_mean) / len(s_mean))

                if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                    JO_fail.append("1")
                    JO_meanlist.append("-9")
                    JO_variance.append("-9")
                else:
                    JO_meanlist.append(mean_JO)
                    JO_variance.append(np.var(s_mean))
               # print(CLC_meanlist)
        except:
            JO_meanlist.append("-9")
            JO_variance.append("-9")
            #mean_AP.append("-9")
            s_fail.append("1")
            JO_fail.append("1")
        store_list = []
        ###Drive City
        try:
            Store = new.loc[new.Store == "WB"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            #print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            WB_fail = []
            if float(len(store_list))==0:
                WB_fail.append("1")
                WB_meanlist.append("-9")
                WB_variance.append("-9")
            else:
                for s in store_list:
                    if float(s) == float("-9"):
                        s_missingv.append("1")
                    else:
                        s_mean.append(s)
                mean_WB = float(sum(s_mean) / len(s_mean))

                if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                    WB_fail.append("1")
                    WB_meanlist.append("-9")
                    WB_variance.append("-9")
                else:
                    WB_meanlist.append(mean_WB)
                    WB_variance.append(np.var(s_mean))
        except:
            WB_meanlist.append("-9")
            WB_variance.append("-9")
            WB_fail.append("1")
        store_list = []
        ###Mindfactory

        ###Mean all
        ### Fail Values rausnehmen

        if float(len(BU_fail))>0:
            mean_BU=float("-9")
        if float(len(JO_fail))>0:
            mean_JO=float("-9")
        if float(len(WB_fail))>0:
            mean_WB=float("-9")



        means = [mean_BU, mean_JO, mean_WB]
        fail=[]
        for mean in means:
            if float(mean)<0:
                fail.append("1")
                print("FAIL")
                print(fail)

        if float(mean_BU)<0:
            fail.append("1")
        if float(mean_JO)<0:
            fail.append("1")
        if float(mean_WB)<0:
            fail.append("1")


        if float(len(fail))>0:
            All_meanlist.append("-9")

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
            BU_rmdlist.append("-9")
            JO_rmdlist.append("-9")
            WB_rmdlist.append("-9")

        else:
            BU_rmd = (mean_BU/min(means))-1
            BU_rmdlist.append(BU_rmd)


            JO_rmd = (mean_JO/min(means))-1
            JO_rmdlist.append(JO_rmd)

            WB_rmd = (mean_WB / min(means)) - 1
            WB_rmdlist.append(WB_rmd)




        # Rmd all
        if float(len(fail))>0:
            All_rmdlist.append("-9")
        else:
            All_rmd = (BU_rmd + JO_rmd + WB_rmd) / 3
            All_rmdlist.append(All_rmd)


        #### Marktdate von Guenstiger.de


        new = part

        Store = new.loc[new.Store == "guen_len"]
        print("Len")
        print(Store)
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
            print("min")
            print(Store)
            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)
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
            print("meanmin")
            print(mean_Min)
            Min_meanlist.append(mean_Min)

                #print(Min_meanlist)
            store_list = []




            ###Maximum

            Store = new.loc[new.Store == "guen_max"]
            print("store-max")
            print(Store)
            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)
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
            print(mean_Max)
            print("meanmax")
            store_list = []

                ###Mean

            Store = new.loc[new.Store == "guen_mean"]
            print("store-mean")
            print(Store)
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
            print(s_mean)
            mean_Mean = float(sum(s_mean) / len(s_mean))
            Mean_meanlist.append(mean_Mean)
            #print(mean_Mean)
                #print(Mean_meanlist)
            store_list = []

                ###0.2 Quantile

            Store = new.loc[new.Store == "guen_q_a"]
            print("store-qa")
            print(Store)
            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)
            s_mean = []
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    pass
                else:
                    s_mean.append(s)
            print(s_mean)
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
            Q_BU.append("-9")
            Q_BUo.append("-9")
            Q_JO.append("-9")
            Q_JOo.append("-9")
            Q_WB.append("-9")
            Q_WBo.append("-9")

        else:
            ### Quitiles CL
            #print("Mean_CL<meanmin")
            #print(mean_CL)
            if float(mean_BU)==float("-9"):
                Q_BU.append("-9")
                Q_BUo.append("-9")
            else:
                if float(mean_BU)<=mean_Min:
                    Q_BU.append("0")
                    Q_BUo.append("0")
                    print(Q_BU)

                if float(mean_BU) <= mean_q2:
                    if float(mean_BU) > mean_Min:
                        Q_BU.append("0,1")
                        Q_BUo.append("1")

                if float(mean_BU) <= mean_q4:
                    if float(mean_BU) > mean_q2:
                        Q_BU.append("0,3")
                        Q_BUo.append("2")

                if float(mean_BU) <= mean_q6:
                    if float(mean_BU) > mean_q4:
                        Q_BU.append("0,5")
                        Q_BUo.append("3")

                if float(mean_BU) <= mean_q8:
                    if float(mean_BU) > mean_q6:
                        Q_BU.append("0,7")
                        Q_BUo.append("4")

                if float(mean_BU) <= mean_Max:
                    if float(mean_BU) > mean_q8:
                        Q_BU.append("0,9")
                        Q_BUo.append("5")

                if float(mean_BU) > mean_Max:
                    Q_BU.append("1")
                    Q_BUo.append("6")

                ### Quitiles CLC
            if float(mean_JO)==float("-9"):
                Q_JO.append("-9")
                Q_JOo.append("-9")
            else:
                if float(mean_JO) <= mean_Min:
                    Q_JO.append("0")
                    Q_JOo.append("0")

                if float(mean_JO) <= mean_q2:
                    if float(mean_JO) > mean_Min:
                        Q_JO.append("0,1")
                        Q_JOo.append("1")

                if float(mean_JO) <= mean_q4:
                    if float(mean_JO) > mean_q2:
                        Q_JO.append("0,3")
                        Q_JOo.append("2")

                if float(mean_JO) <= mean_q6:
                    if float(mean_JO) > mean_q4:
                        Q_JO.append("0,5")
                        Q_JOo.append("3")

                if float(mean_JO) <= mean_q8:
                    if float(mean_JO) > mean_q6:
                        Q_JO.append("0,7")
                        Q_JOo.append("4")

                if float(mean_JO) <= mean_Max:
                    if float(mean_JO) > mean_q8:
                        Q_JO.append("0,9")
                        Q_JOo.append("5")

                if float(mean_JO) > mean_Max:
                    Q_JO.append("1")
                    Q_JOo.append("6")

                ###DM
                #####'''''''
            if float(mean_WB) == float("-9"):
                Q_WB.append("-9")
                Q_WBo.append("-9")
            else:
                ### Quitiles AP

                if float(mean_WB) <= mean_Min:
                    Q_WB.append("0")
                    Q_WBo.append("0")

                if float(mean_WB) <= mean_q2:
                    if float(mean_WB) > mean_Min:
                        Q_WB.append("0,1")
                        Q_WBo.append("1")

                if float(mean_WB) <= mean_q4:
                    if float(mean_WB) > mean_q2:
                        Q_WB.append("0,3")
                        Q_WBo.append("2")

                if float(mean_WB) <= mean_q6:
                    if float(mean_WB) > mean_q4:
                        Q_WB.append("0,5")
                        Q_WBo.append("3")

                if float(mean_WB) <= mean_q8:
                    if float(mean_WB) > mean_q6:
                        Q_WB.append("0,7")
                        Q_WBo.append("4")

                if float(mean_WB) <= mean_Max:
                    if float(mean_WB) > mean_q8:
                        Q_WB.append("0,9")
                        Q_WBo.append("5")

                if float(mean_WB) > mean_Max:
                    Q_WB.append("1")
                    Q_WBo.append("6")




        ###store means ranks
        new = part.drop(part.index[[3, 4, 5, 6, 7, 8, 9, 10]])
        #print(Store)
        base = new.iloc[:, 0]

        #print(base)

        base_list = []

        #print(base_list)
        ## data for parametric test
        add_list = []
        ### data for non parametric test

        ranking_stores = ["r_BU", "r_JO","r_WB",]
        df_ranking = pd.DataFrame(ranking_stores)

        ## Ranking lists

        r_BU = []
        r_JO = []
        r_WB = []



        no_diff =[]
        yes_diff=[]

        for b in range(3, 56):
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

                if np_list[0]==np_list[1]==np_list[2]:
                    no_diff.append("1")
                else:
                    yes_diff.append("1")

                r_BU.append(np_list[0])
                r_JO.append(np_list[1])
                r_WB.append(np_list[2])

                #print(r_CL)
                #print(r_CLC)
                #print(r_MF)




        if len(r_BU) < 20:
            BU_meanr.append("-9")
            JO_meanr.append("-9")
            WB_meanr.append("-9")

            diff_rate.append("-9")
        else:
            BU_meanr.append(sum(r_BU)/len(r_BU))
            JO_meanr.append(sum(r_JO)/len(r_JO))
            WB_meanr.append(sum(r_WB)/len(r_WB))

            #print(len(yes_diff))
            #print(len(r_CL))
            diff_rate.append(len(yes_diff)/len(r_BU))




print(len(Id_list))
print(len(BU_meanlist))
print(len(JO_meanlist))
print(len(WB_meanlist))

print(len(Len_meanlist))
print(Len_meanlist)
print(len(Min_meanlist))
print(Min_meanlist)
print(len(Max_meanlist))
print(Max_meanlist)
print(len(Q2_meanlist))
print(Q2_meanlist)
print(len(Q4_meanlist))
print(Q4_meanlist)
print(len(Q6_meanlist))
print(Q6_meanlist)
print(len(Q8_meanlist))
print(Q8_meanlist)

print(len(Q_BU))
print(len(Q_BUo))
print(Q_BU)
print(Q_BUo)
print(len(Q_JO))
print(len(Q_JOo))
print(Q_JO)
print(Q_JOo)
print(len(Q_WB))
print(len(Q_WBo))
print(Q_WB)
print(Q_WBo)

#dfend = pd.DataFrame({'EAN': Id_list, "mean_BU":BU_meanlist,"var_BU":BU_variance,"mean_JO":JO_meanlist,"var_JO":JO_variance,
#                      "mean_WB":WB_meanlist,"var_WB":WB_variance,
#                       "meanr_BU":BU_meanr,"meanr_JO":JO_meanr,"meanr_WB":WB_meanr,"diff_rate":diff_rate,
#                      "All_rmd":All_rmdlist, "BU_rmd":BU_rmdlist,"JO_rmd":JO_rmdlist,"WB_rmd":WB_rmdlist,
#                      "All_mean":All_meanlist,"Low1p":Low1p_meanlist,"Low2p":Low2p_meanlist,"Midp":Midp_meanlist,"Highp":Highp_meanlist,
#                      "Len_mp":Len_meanlist, "Min_mp":Min_meanlist, "Max_mp":Max_meanlist, "Mean_mp":Mean_meanlist, "Q2_mp":Q2_meanlist,"Q4_mp":Q4_meanlist,"Q6_mp":Q6_meanlist,"Q8_mp":Q8_meanlist,
#                      "Q_BU":Q_BU,"Q_BUo":Q_BUo, "Q_JO":Q_JO, "Q_JOo":Q_JOo,"Q_WB":Q_WB,"Q_WBo":Q_WBo,
#                     })

#dfend.to_excel('DF_WBCleaning_early.xlsx')
d = dict( EAN = np.array(Id_list), Mean_BU = np.array(BU_meanlist),Var_BU = np.array(BU_variance),Mean_JO = np.array(JO_meanlist),Var_JO = np.array(JO_variance),Mean_WB = np.array(WB_meanlist),Var_WB = np.array(WB_variance),
          BU_Meanr = np.array(BU_meanr),JO_Meanr = np.array(JO_meanr),WB_Meanr = np.array(WB_meanr),Dif_Rate = np.array(diff_rate),
          RMD_ALL = np.array(All_rmdlist), RMD_BU = np.array(BU_rmdlist),RMD_JO = np.array(JO_rmdlist),RMD_WB = np.array(WB_rmdlist),
          Mean_ALL = np.array(All_meanlist),Lowp1 = np.array(Low1p_meanlist),Lowp2 = np.array(Low2p_meanlist),Midp = np.array(Midp_meanlist),Highp = np.array(Highp_meanlist),
          #R = np.array(Highp_meanlist),S = np.array(Highp_meanlist),T = np.array(Highp_meanlist),U = np.array(Highp_meanlist),V = np.array(Highp_meanlist),
          Len_MP = np.array(Len_meanlist),Min_MP = np.array(Min_meanlist),Max_MP = np.array(Max_meanlist),Mean_MP = np.array(Mean_meanlist),Q2_MP = np.array(Q2_meanlist),Q4_MP = np.array(Q4_meanlist),Q6_MP = np.array(Q6_meanlist),Q8_MP = np.array(Q8_meanlist),
          Q_BU = np.array(Q_BU),Qo_BU = np.array(Q_BUo),Q_JO = np.array(Q_JO),Qo_JO = np.array(Q_JOo),Q_WB = np.array(Q_WB),Qo_WB = np.array(Q_WBo),
          )
dfend=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))

dfend.to_excel('DF_WBCleaning_late.xlsx')