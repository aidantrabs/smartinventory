import pandas as pd
import csv, math
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm, model_selection
import numpy as np

# import sqlite3

class LinReg:

    X = None
    y = None
    df = None

    def __init__(self, filename):
        df = pd.csv_read( filename )
        df = df[['item_id', 'item_price', 'item_cnt_day', 'date']]
        if df.columns < 4: #hmm I think it will always have columns just some of them are na... i believe once its completely blank its not registered
            raise Exception( "The file is not in the right format" )
        self.df = df

    def Calculate( self ):
        # Our issue is that we need to find the 30 days for a specific product/item. 
        # so we're first organizing by date and then by item_id 
        # we will end up with groupings of item that are then grouped by date 
        # and then for each item we will train for that particular dataset
        # and return the predicted 30 day usage from there


        #another issue is that we actually need to find the starting date, and count the number of days
        #because items used should be linear with the number of days 
        #we should also probably have a cumulative items bought rather than just the item count 

        return self.df.head() #just to see if this works 

        #aribitrarily we will take the frist entry to be our "day zero"
        start_date = pd.to_datetime( self.df.iloc[1]['date'] )
        dates = pd.to_datetime( self.df['date'] ) - start_date
        self.df['date'] = dates.dt.days #the dates column now has the number of days from day zero, rather than the actual date

        #hmm I should probably test this on my own before we come and try to put it together 

        df_grouped = self.df.groupby( 'date', 'item_id' )

        for item_id, data in df_grouped: #i have no idea if this is the right formatting for the data. We will see. 
            prediction = self.Train( data )
            output.append( [item_id, prediction ] )
        return output

    #anyway, for train I will just assume we have the data in the neccessary format
    #
    def Train( self, df ): 
        
        
        forecast_col = 'item_cnt_day' 

        df.fillna( -99999, inplace=True ) #probably not needed for us since we're guaranteed that all the columns have values

        forecast_out = 30 # We want to predict 30 days into the future

        df['label'] = df[forecast_col].shift(-forecast_out) #this literally shifts the columns up by 30. 
        #we're making a lot of assumptions here, like we're not looking at more than one per day
        #and there aren't days where there aren't any 
        #Technically we should have inputted rows for every day and if there aren't any then there should be 0 that day
        #but we can just assume that the data is in the right formatting, right? 
        #if not we can probably find a way to add it in in the calculate function above, riiiight? 

        df.dropna( inplace = True)

        self.X = np.array( df.drop['label'] )

        self.X = preprocessing.scale( self.X )
        self.X = self.X[:-forecast_out+1]
        df.dropna( inplace = True )

        self.y = np.array( df['label'] )



        X_train, X_test, y_train, y_test = model_selection.train_test_split(self.X, self.y, test_size=0.2)

        clf = LinearRegression()
        clf.fit( X_train, y_train )
        accuracy = clf.score( X_test, y_test )

        #see I have no idea if this will work... we just took the youtube video code and ran with it 

        return accuracy
        
        # what are we trying to predict? item_cnt_day and price?

        #the item_cnt_day for the next 30 days 
        #bascially how much they need to buy for inventory the next month 
        #price is important though because price will likely affect sales volume


        return accuracy
        
        # what are we trying to predict? item_cnt_day and price?

        #the item_cnt_day for the next 30 days 
        #bascially how much they need to buy for inventory the next month 
        #price is important though because price will likely affect sales volume


        return accuracy
        
        # what are we trying to predict? item_cnt_day and price?

        #the item_cnt_day for the next 30 days 
        #bascially how much they need to buy for inventory the next month 
        #price is important though because price will likely affect sales volume


        return accuracy
        
        # what are we trying to predict? item_cnt_day and price?

        #the item_cnt_day for the next 30 days 
        #bascially how much they need to buy for inventory the next month 
        #price is important though because price will likely affect sales volume


        return accuracy
        
        # what are we trying to predict? item_cnt_day and price?

        #the item_cnt_day for the next 30 days 
        #bascially how much they need to buy for inventory the next month 
        #price is important though because price will likely affect sales volume


        return accuracy
        
        # what are we trying to predict? item_cnt_day and price?

        #the item_cnt_day for the next 30 days 
        #bascially how much they need to buy for inventory the next month 
        #price is important though because price will likely affect sales volume


        return accuracy
        
        # what are we trying to predict? item_cnt_day and price?

        #the item_cnt_day for the next 30 days 
        #bascially how much they need to buy for inventory the next month 
        #price is important though because price will likely affect sales volume

        # hmm so item cnt vs date then and use price as the error factor?

        #smth like that what do you mean error factor? 
        #to account for any annomolys in real world scenarios (more accurate data) - the model is essentially data = model + error (according to 
        # crash course stats :P)

        #hehe that's hackathons pretty much crash course everything 
        #yeah that sounds about right

        




