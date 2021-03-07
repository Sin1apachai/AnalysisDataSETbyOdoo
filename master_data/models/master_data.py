# -*- coding: utf-8 -*-
from odoo import models, fields, api
import pandas as pd

class PTTData(models.Model):
    _name = 'data.ptt'
    _description = "Data of PTT From SET"

    @api.model
    def push_data(self):
        dataframe_ptt = pd.read_html("https://www.set.or.th/set/historicaltrading.do?symbol=PTT&ssoPageId=2&language=th&country=TH")[0]
        for data in dataframe_ptt.iloc[:, [0,1,2,3,4]].values.tolist():
            vals = {}
            vals['dd'] =  data[0]
            vals['po'] = data[1]
            vals['ph'] = data[2]
            vals['pl'] = data[3]
            vals['pc'] =  data[4]
            self.create(vals)

    dd = fields.Text(string="Date Data")
    ph = fields.Float(string="Price High")
    pl = fields.Float(string="Price Low")
    po = fields.Float(string="Price Open")
    pc = fields.Float(string="Price Close")
