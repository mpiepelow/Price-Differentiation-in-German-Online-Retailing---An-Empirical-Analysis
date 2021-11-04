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
##store means
CL_meanlist=[]
CL_variance=[]
CLC_meanlist=[]
CLC_variance=[]
DC_meanlist=[]
DC_variance=[]
MF_meanlist=[]
MF_variance=[]
MFC_meanlist=[]
MFC_variance=[]
VO_meanlist=[]
VO_variance=[]

### store mean rankings

CL_meanr =[]
CLC_meanr =[]
DC_meanr =[]
MF_meanr =[]
MFC_meanr =[]
VO_meanr =[]

## defferentiation rate
diff_rate =[]

with open("C:/Users/Euronymus/Desktop/Scrapeyscrapey/selenium test/datasample_Mindfactory.csv", 'r') as file:
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
allproducts = pd.read_excel('C:/Users/Euronymus/Desktop/Scrapeyscrapey/selenium test/Dataframes/Mindfactory/Mindfactory/Dataframe_early_Mindfactory_a.xlsx', index_col=0,
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

        #### Reduce to only stores ###

        new = part.drop(part.index[[6, 7, 8, 9, 10, 11, 12]])
        print(new)
        ## Compuland
        #Stores = ["CL", "CLC", "DC", "MF", "MFC", "VO"]
        ## Mean and CLeaning of stores
        try:
            Store = new.loc[new.Store == "CL"]



            store_list = []

            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)

            s_mean=[]
            s_missingv=[]
            s_fail=[]
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            print(s_mean)
            mean_CL = float(sum(s_mean)/len(s_mean))

            #missing.append(len(s_missingv))

            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                s_fail.append("1")
                Cl_meanlist.append("-9")
                CL_variance.append("-9")
            else:
                CL_meanlist.append(mean_CL)
                CL_variance.append(np.var(s_mean))
        except:
            CL_meanlist.append("-9")
            CL_variance.append("-9")
            s_fail.append("1")
        print("CL")
        print(mean_CL)
        store_list = []
        ###Compuland City
        try:
            Store = new.loc[new.Store == "CLC"]

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
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            print(s_mean)
            mean_CLC = float(sum(s_mean)/len(s_mean))
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                s_fail.append("1")
                ClC_meanlist.append("-9")
                CLC_variance.append("-9")
            else:
                CLC_meanlist.append(mean_CLC)
                CLC_variance.append(np.var(s_mean))
            print(CLC_meanlist)
        except:
            CLC_meanlist.append("-9")
            CLC_variance.append("-9")
            s_fail.append("1")
        store_list = []
        ###Drive City
        try:
            Store = new.loc[new.Store == "DC"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)
            s_mean =[]
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_DC = float(sum(s_mean)/len(s_mean))
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                s_fail.append("1")
                DC_meanlist.append("-9")
                DC_variance.append("-9")
            else:
                DC_meanlist.append(mean_DC)
                DC_variance.append(np.var(s_mean))
        except:
            DC_meanlist.append("-9")
            DC_variance.append("-9")
            s_fail.append("1")
        store_list = []
        ###Mindfactory
        try:
            Store = new.loc[new.Store == "MF"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)
            s_mean =[]
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_MF = float(sum(s_mean)/len(s_mean))
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                s_fail.append("1")
                MF_meanlist.append("-9")
                MF_variance.append("-9")
            else:
                MF_meanlist.append(mean_MF)
                MF_variance.append(np.var(s_mean))
        except:
            MF_meanlist.append("-9")
            MF_variance.append("-9")
            s_fail.append("1")
        store_list = []
        ###Mindfactory City
        try:
            Store = new.loc[new.Store == "MFC"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)
            s_mean =[]
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_MFC = float(sum(s_mean)/len(s_mean))
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                s_fail.append("1")
                MFC_meanlist.append("-9")
                MFC_variance.append("-9")
            else:
                MFC_meanlist.append(mean_MFC)
                MFC_variance.append(np.var(s_mean))
            #print(s_mean)
            #print(s_missingv)
            #print(len(store_list))
            #print(len(s_missingv))
        except:
            MFC_meanlist.append("-9")
            MFC_variance.append("-9")
            s_fail.append("1")
        print(MFC_meanlist)
        store_list = []
        ###Vibu Online
        try:
            Store = new.loc[new.Store == "VO"]

            store_list = []
            for store in Store.iloc[0, :]:
                store_list.append(store)
            store_list.pop(0)
            store_list.pop(0)
            print(store_list)
            s_mean =[]
            s_missingv = []
            s_fail = []
            for s in store_list:
                if float(s) == float("-9"):
                    s_missingv.append("1")
                else:
                    s_mean.append(s)
            mean_VO = float(sum(s_mean)/len(s_mean))
            if (float((len(store_list)) - float(len(s_missingv)))) < 20:
                s_fail.append("1")
                VO_meanlist.append("-9")
                VO_variance.append("-9")
            else:
                VO_meanlist.append(mean_VO)
                VO_variance.append(np.var(s_mean))
            print(VO_meanlist)
        except:
            VO_meanlist.append("-9")
            VO_variance.append("-9")
            s_fail.append("1")
        ###store means

        print(Store)
        base = new.iloc[:, 0]

        print(base)

        base_list = []

        print(base_list)
        ## data for parametric test
        add_list = []
        ### data for non parametric test

        ranking_stores = ["r_CL", "r_CLC","r_DC","r_MF", "r_MFC","r_VO"]
        df_ranking = pd.DataFrame(ranking_stores)

        ## Ranking lists

        r_CL = []
        r_CLC = []
        r_DC = []
        r_MF = []
        r_MFC = []
        r_VO = []


        no_diff =[]
        yes_diff=[]
        for b in range(3, 58):
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

            ### ranking
            else:
                np_list = []
                s = pd.Series(addon)
                q = s.rank(method='dense')
                for s in q:
                    np_list.append(s)

                print(np_list)
            ###check for no differentiation

                if np_list[0]==np_list[1]==np_list[2]==np_list[3]==np_list[4]==np_list[5]:
                    no_diff.append("1")
                else:
                    yes_diff.append("1")

                r_CL.append(np_list[0])
                r_CLC.append(np_list[1])
                r_DC.append(np_list[2])
                r_MF.append(np_list[3])
                r_MFC.append(np_list[4])
                r_VO.append(np_list[5])

                print(r_CL)
                print(r_CLC)
                print(r_MF)


        if len(r_CL) < 20:
            CL_meanr.append("-9")
            CLC_meanr.append("-9")
            DC_meanr.append("-9")
            MF_meanr.append("-9")
            MFC_meanr.append("-9")
            VO_meanr.append("-9")
            diff_rate.append("-9")
        else:
            CL_meanr.append(sum(r_CL)/len(r_CL))
            CLC_meanr.append(sum(r_CLC)/len(r_CLC))
            DC_meanr.append(sum(r_DC)/len(r_DC))
            MF_meanr.append(sum(r_MF)/len(r_MF))
            MFC_meanr.append(sum(r_MFC)/len(r_MFC))
            VO_meanr.append(sum(r_VO)/len(r_VO))
            #print(len(yes_diff))
            #print(len(r_CL))
            diff_rate.append(len(yes_diff)/len(r_CL))
        print(CL_meanr)
        print(CLC_meanr)
        print(diff_rate)
        #print(hurensiohn)

#            df = pd.concat([df,df1], ignore_index=True, axis=1)
#            print("partlist")
#            print(part_list)
#            ### means of lists variances --> ende goßer data frame und dann df to excel
#            ## ranking for np tests
#            s = pd.Series(part_list)
#            q = s.rank(method='dense')
#            # print(s)
#            # print(q)
#            for s in q:
#                np_list.append(s)

            ####minimum relation for parametric tests
#            minimum = min(part_list)
#            for d in part_list:
#                entry = float(d) - float(minimum)


 #               add_list.append(entry)





            #### Dataframe for parametric tests
            #df = pd.DataFrame({'Store': base_list,
            #                   'Price': add_list,
            #                   })
            #print(df)

            ### dataframe for non parametric tests
            #dfnp = pd.DataFrame({'Store': base_list,
            #                     'Price': np_list
            #                     })
            #print(dfnp)

            # bp = df.boxplot('Price', by='Store')
            # print(bp)












print(len(Id_list))
#CL_meanlist = list(dict.fromkeys(CL_meanlist))
print(len(CL_meanlist))
#CLC_meanlist = list(dict.fromkeys(CLC_meanlist))
print(len(CLC_meanlist))
#DC_meanlist = list(dict.fromkeys(DC_meanlist))
print(len(DC_meanlist))
#MF_meanlist = list(dict.fromkeys(MF_meanlist))
print(len(MF_meanlist))
#MFC_meanlist = list(dict.fromkeys(MFC_meanlist))
print(len(MFC_meanlist))
#VO_meanlist = list(dict.fromkeys(VO_meanlist))
print(len(VO_meanlist))


dfend = pd.DataFrame({'EAN': Id_list, "mean_CL":CL_meanlist,"var_CL":CL_variance,"mean_CLC":CLC_meanlist,"var_CLC":CLC_variance,
                      "mean_DC":DC_meanlist,"var_DC":DC_variance,"mean_MF":MF_meanlist,"var_MF":MF_variance, "mean_MFC":MFC_meanlist,"var_MFC":MFC_variance, "mean_VO":VO_meanlist, "var_VO":VO_variance,
                       "meanr_CL":CL_meanr,"meanr_CLC":CLC_meanr,"meanr_DC":DC_meanr,"meanr_MF":MF_meanr,"meanr_MFC":MFC_meanr,"meanr_VO":VO_meanr,"diff_rate":diff_rate
                     })

dfend.to_excel('DF_Cleaning_early.xlsx')