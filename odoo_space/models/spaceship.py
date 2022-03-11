# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = 'space.spaceship'
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Title', required= True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Priority',
                             selection=[('low', 'Low'),
                                        ('medium', 'Medium'),
                                        ('high', 'High')],
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)     
