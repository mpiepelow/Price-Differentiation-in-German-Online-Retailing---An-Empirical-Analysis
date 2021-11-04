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
TH_meanlist=[]
TH_variance=[]
BO_meanlist=[]
BO_variance=[]
Checked =[]
All_meanlist=[]
### Preishöhen
Low1p_meanlist=[]
Low2p_meanlist=[]
Midp_meanlist=[]
Highp_meanlist=[]
##Minimum Distence
TH_rmdlist=[]
BO_rmdlist=[]


All_rmdlist=[]


### Quintiles

Q_TH =[]
Q_THo =[]
Q_BO =[]
Q_BOo =[]



### store mean rankings

TH_meanr =[]
BO_meanr =[]


## defferentiation rate
diff_rate =[]

###shit check
triggered=[]

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
allproducts = pd.read_excel('C:/Users/Euronymus/Desktop/Scrapeyscrapey/selenium test/Dataframes/Mindfactory/Thalia/Dataframe_late_Thalia.xlsx', index_col=0,
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
            Store = new.loc[new.Store == "TH"]

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
            mean_TH = float(sum(s_mean) / len(s_mean))

            # missing.append(len(s_missingv))
            TH_fail=[]
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                TH_fail.append("1")
                TH_meanlist.append("-9")
                TH_variance.append("-9")
            else:
                TH_meanlist.append(mean_TH)
                TH_variance.append(np.var(s_mean))
        except:
            TH_meanlist.append("-9")
            TH_variance.append("-9")
            s_fail.append("1")
        #print("CL")
        #print(mean_CL)
        store_list = []
        ###Compuland City
        try:
            Store = new.loc[new.Store == "BO"]

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
            mean_BO = float(sum(s_mean) / len(s_mean))
            BO_fail=[]
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                BO_fail.append("1")
                BO_meanlist.append("-9")
                BO_variance.append("-9")
            else:
                BO_meanlist.append(mean_BO)
                BO_variance.append(np.var(s_mean))
           # print(CLC_meanlist)
        except:
            BO_meanlist.append("-9")
            BO_variance.append("-9")
            #mean_AP.append("-9")
            s_fail.append("1")
        store_list = []


        ###Mean all
        ### Fail Values rausnehmen

        if float(len(TH_fail))>0:
            mean_TH=float("-9")
        if float(len(BO_fail))>0:
            mean_BO=float("-9")



        means = [mean_TH, mean_BO]
        fail=[]
        for mean in means:
            if float(mean)<0:
                fail.append("1")
                print("FAIL")
                print(fail)

        if float(mean_TH)<0:
            fail.append("1")
        if float(mean_BO)<0:
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
            if All_mean<=10:
                Low1p_meanlist.append("1")
                Low2p_meanlist.append("0")
                Midp_meanlist.append("0")
                Highp_meanlist.append("0")
            if All_mean<=30:
                if All_mean>10:
                    Low1p_meanlist.append("0")
                    Low2p_meanlist.append("1")
                    Midp_meanlist.append("0")
                    Highp_meanlist.append("0")
            if All_mean<=100:
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
            TH_rmdlist.append("-9")
            BO_rmdlist.append("-9")

        else:
            TH_rmd = (mean_TH/min(means))-1
            TH_rmdlist.append(TH_rmd)


            BO_rmd = (mean_BO/min(means))-1
            BO_rmdlist.append(BO_rmd)





        # Rmd all
        if float(len(fail))>0:
            All_rmdlist.append("-9")
        else:
            All_rmd = (TH_rmd + BO_rmd) / 2
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
        check=[]
        if float(mean_Len)==float("-9"):
            Q_TH.append("-9")
            Q_THo.append("-9")
            Q_BO.append("-9")
            Q_BOo.append("-9")
            check.append("1")
        else:
            ### Quitiles CL

            if float(mean_TH)==float("-9"):
                Q_TH.append("-9")
                Q_THo.append("-9")
                #check.append("1")
            else:
                if float(mean_TH)<=mean_Min:
                    Q_TH.append("0")
                    Q_THo.append("0")
                    print(Q_TH)
                    #check.append("1")

                if float(mean_TH) <= mean_q2:
                    if float(mean_TH) > mean_Min:
                        Q_TH.append("0,1")
                        Q_THo.append("1")
                        #check.append("1")

                if float(mean_TH) <= mean_q4:
                    if float(mean_TH) > mean_q2:
                        Q_TH.append("0,3")
                        Q_THo.append("2")
                        #check.append("1")

                if float(mean_TH) <= mean_q6:
                    if float(mean_TH) > mean_q4:
                        Q_TH.append("0,5")
                        Q_THo.append("3")
                        #check.append("1")

                if float(mean_TH) <= mean_q8:
                    if float(mean_TH) > mean_q6:
                        Q_TH.append("0,7")
                        Q_THo.append("4")
                        #check.append("1")

                if float(mean_TH) <= mean_Max:
                    if float(mean_TH) > mean_q8:
                        Q_TH.append("0,9")
                        Q_THo.append("5")
                        #check.append("1")

                if float(mean_TH) > mean_Max:
                    Q_TH.append("1")
                    Q_THo.append("6")
                    #check.append("1")
                #print(Q_TH)
            #if float(len(check))> 1:
                #Q_TH.pop(-1)
                #Q_THo.pop(-1)


                ### Quitiles BO
            #check = []
            if float(mean_BO)==float("-9"):
                Q_BO.append("-9")
                Q_BOo.append("-9")
                check.append("1")
            else:
                if EAN == "9789463593168":
                    Q_BO.append("-9")
                    Q_BOo.append("-9")
                    check.append("1")
                else:
                    if float(mean_BO) <= mean_Min:
                        Q_BO.append("0")
                        Q_BOo.append("0")
                        check.append("1")
                    if float(mean_BO) <= mean_q2:
                        if float(mean_BO) > mean_Min:
                            Q_BO.append("0,1")
                            Q_BOo.append("1")
                            check.append("1")
                    if float(mean_BO) <= mean_q4:
                        if float(mean_BO) > mean_q2:
                            Q_BO.append("0,3")
                            Q_BOo.append("2")
                            check.append("1")
                    if float(mean_BO) <= mean_q6:
                        if float(mean_BO) > mean_q4:
                            Q_BO.append("0,5")
                            Q_BOo.append("3")
                            check.append("1")
                    if float(mean_BO) <= mean_q8:
                        if float(mean_BO) > mean_q6:
                            Q_BO.append("0,7")
                            Q_BOo.append("4")
                            check.append("1")
                    if float(mean_BO) <= mean_Max:
                        if float(mean_BO) > mean_q8:
                            Q_BO.append("0,9")
                            Q_BOo.append("5")
                            check.append("1")
                    if float(mean_BO) > mean_Max:
                        Q_BO.append("1")
                        Q_BOo.append("6")
                        check.append("1")
                    print(Q_BO)
                if float(len(check))!= 1:
                    #Q_BO.append("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    #Q_BOo.append("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    Checked.append("1")
                    Checked.append(EAN)
                    Checked.append(len(check))
                if float(len(check))== 1:
                    triggered.append("1")
            #if len(Succ)<1:
            #    Q_ZR.append("-9")
            #    Q_ZRo.append("-9")


        ###store means ranks
        new = part.drop(part.index[[2, 3, 4, 5, 6, 7, 8, 9]])
        #print(Store)
        base = new.iloc[:, 0]

        #print(base)

        base_list = []

        #print(base_list)
        ## data for parametric test
        add_list = []
        ### data for non parametric test

        ranking_stores = ["r_TH", "r_BO"]
        df_ranking = pd.DataFrame(ranking_stores)

        ## Ranking lists

        r_TH = []
        r_BO = []


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

                if np_list[0]==np_list[1]:
                    no_diff.append("1")
                else:
                    yes_diff.append("1")

                r_TH.append(np_list[0])
                r_BO.append(np_list[1])


                #print(r_CL)
                #print(r_CLC)
                #print(r_MF)




        if len(r_TH) < 20:
            TH_meanr.append("-9")
            BO_meanr.append("-9")

            diff_rate.append("-9")
        else:
            TH_meanr.append(sum(r_TH)/len(r_TH))
            BO_meanr.append(sum(r_BO)/len(r_BO))
                        #print(len(yes_diff))
            #print(len(r_CL))
            diff_rate.append(len(yes_diff)/len(r_TH))




print(len(Id_list))
print(len(TH_meanlist))
print(len(BO_meanlist))


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

print(len(Q_TH))
print(len(Q_THo))
print(Q_BO)
print(Q_BOo)
print(Checked)
print(len(triggered))
#dfend = pd.DataFrame({'EAN': Id_list, "mean_TH":TH_meanlist,"var_TH":TH_variance,"mean_BO":BO_meanlist,"var_BO":BO_variance,
#                      "meanr_TH":TH_meanr,"meanr_BO":BO_meanr,"diff_rate":diff_rate,
#                      "All_rmd":All_rmdlist, "TH_rmd":TH_rmdlist,"BO_rmd":BO_rmdlist,
#                      "All_mean":All_meanlist,"Low1p":Low1p_meanlist,"Low2p":Low2p_meanlist,"Midp":Midp_meanlist,"Highp":Highp_meanlist,
#                      "Len_mp":Len_meanlist, "Min_mp":Min_meanlist, "Max_mp":Max_meanlist, "Mean_mp":Mean_meanlist, "Q2_mp":Q2_meanlist,"Q4_mp":Q4_meanlist,"Q6_mp":Q6_meanlist,"Q8_mp":Q8_meanlist,
#                      "Q_TH":Q_TH,"Q_THo":Q_THo, "Q_BO":Q_BO, "Q_BOo":Q_BOo,
#                     })
d = dict( EAN = np.array(Id_list), Mean_TH = np.array(TH_meanlist),Var_TH = np.array(TH_variance),Mean_BO = np.array(BO_meanlist),Var_BO = np.array(BO_variance),
          TH_Meanr = np.array(TH_meanr),BO_Meanr = np.array(BO_meanr),Dif_Rate = np.array(diff_rate),
          RMD_ALL = np.array(All_rmdlist), RMD_TH = np.array(TH_rmdlist),RMD_BO = np.array(BO_rmdlist),
          Mean_ALL = np.array(All_meanlist),Lowp1 = np.array(Low1p_meanlist),Lowp2 = np.array(Low2p_meanlist),Midp = np.array(Midp_meanlist),Highp = np.array(Highp_meanlist),
          #R = np.array(Highp_meanlist),S = np.array(Highp_meanlist),T = np.array(Highp_meanlist),U = np.array(Highp_meanlist),V = np.array(Highp_meanlist),
          Len_MP = np.array(Len_meanlist),Min_MP = np.array(Min_meanlist),Max_MP = np.array(Max_meanlist),Mean_MP = np.array(Mean_meanlist),Q2_MP = np.array(Q2_meanlist),Q4_MP = np.array(Q4_meanlist),Q6_MP = np.array(Q6_meanlist),Q8_MP = np.array(Q8_meanlist),
          Q_TH = np.array(Q_TH),Qo_TH = np.array(Q_THo),Q_BO = np.array(Q_BO),Qo_BO = np.array(Q_BOo),
          )
dfend=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))

dfend.to_excel('DF_THCleaning_late.xlsx')
