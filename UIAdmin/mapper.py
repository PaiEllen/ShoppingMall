#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Infrastructure.DI import Meta
from Model.User import UserService
from Repository.Admin.UserRepository import UserRepository
from Model.Region import RegionService
from Repository.Admin.RegionRepository import RegionRepository
from Model.User import CustomerService

Meta.DIMapper.inject(UserService,UserRepository())
Meta.DIMapper.inject(RegionService,RegionRepository())
Meta.DIMapper.inject(CustomerService,UserRepository())
