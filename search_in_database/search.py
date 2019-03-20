__author__ = 'willian.reis'
import os
import datetime

class cSearch():
    df = None
    number_f_company = 0
    def __init__(self, data):
        self.df = data


    def ProcessSearch(self, product, company_state):
        if product != '':
            self.df = self.df[self.df.product_list_product.map(lambda x: product in x)]

        if company_state != '':
            self.df = self.df[self.df.company_state.map(lambda x: company_state in x)]

        path = os.getcwd() + '\\busca_'+ str(datetime.datetime.now().time().strftime('%HH_%MM_%SS'))
        print 'As buscas podem ser encontradas em ', path

        print 'Busca realizada por ' + product + ' em ' + company_state
        if self.df.empty:
            print 'Nao ha itens para esta pesquisa'
            exit()

        print 'Quantidade total de empresas encontradas: ',  len(self.df.company_Id.unique())
        self.number_f_company = len(self.df.company_Id.unique())

        filename = str(datetime.datetime.now().date()) +'_'+str(len(self.df.company_Id.unique()))+ '.csv'
        os.mkdir(path)
        self.df.to_csv(path + "\\" + filename)

        print 'Descricao de todas as empresas localizadas: '
        print "product | company_Id | product_price | company_state"
        for ccompany_id in self.df.company_Id.unique():
            df_company = self.df
            df_company = df_company[df_company['company_Id'] == ccompany_id]

            filename_company = str(datetime.datetime.now().date()) +'_'+ccompany_id+'.csv'
            df_company.to_csv(path + "\\" + filename_company)
            for index, row in df_company.iterrows():
                print  df_company['product_list_product'][index], '|', df_company['company_Id'][index],'|', df_company['product_list_product_price'][index], '|', df_company['company_state'][index]