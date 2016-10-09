#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
from UIAdmin.Controllers import Account
from UIAdmin.Controllers import Region
from UIAdmin.Controllers import Customer
from UIAdmin.Controllers import Merchant
from UIAdmin import mapper

settings = {
    'template_path': 'Views',
    'static_path': 'Statics',
    'static_url_prefix': '/statics/',
}
application = tornado.web.Application([
    # (r"/index", Account.IndexHandler),
    (r"/login", Account.LoginHandler),
    (r"/check", Account.CheckCodeHandler),
    (r"/ProvinceManager.html$", Region.ProvinceManagerHandler),
    (r"/province.html$", Region.ProvinceHandler),
    (r"/CityManager.html$", Region.CityManagerHandler),
    (r"/City.html$", Region.CityHandler),
    (r"/CountyManager.html$", Region.CountyManagerHandler),
    (r"/County.html$", Region.CountyHandler),
    (r"/CustomerManager.html$", Customer.CustomerManagerHandler),
    (r"/customer.html$", Customer.CustomerHandler),
    (r"/MerchantManager.html$", Merchant.MerchantManagerHandler),
    (r"/Merchant.html$", Merchant.MerchantHandler),
    (r"/MerchantEdit.html$", Merchant.MerchantEditHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()