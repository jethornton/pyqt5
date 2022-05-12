#!/usr/bin/python3

from PyQt5 import QtCore
from PyQt5.QtCore import QStandardPaths

std_paths_list_names = ['QStandardPaths.DesktopLocation',
		'QStandardPaths.DocumentsLocation',
		'QStandardPaths.FontsLocation',
		'QStandardPaths.ApplicationsLocation',
		'QStandardPaths.MusicLocation',
		'QStandardPaths.MoviesLocation',
		'QStandardPaths.PicturesLocation',
		'QStandardPaths.TempLocation',
		'QStandardPaths.HomeLocation',
		'QStandardPaths.DataLocation',
		'QStandardPaths.AppLocalDataLocation',
		'QStandardPaths.CacheLocation',
		'QStandardPaths.GenericDataLocation',
		'QStandardPaths.RuntimeLocation',
		'QStandardPaths.ConfigLocation',
		'QStandardPaths.DownloadLocation',
		'QStandardPaths.GenericCacheLocation',
		'QStandardPaths.GenericConfigLocation',
		'QStandardPaths.AppDataLocation',
		'QStandardPaths.AppConfigLocation']

# QStandardPaths is a constant (number)
std_paths_list = [QStandardPaths.DesktopLocation,
		QStandardPaths.DocumentsLocation,
		QStandardPaths.FontsLocation,
		QStandardPaths.ApplicationsLocation,
		QStandardPaths.MusicLocation,
		QStandardPaths.MoviesLocation,
		QStandardPaths.PicturesLocation,
		QStandardPaths.TempLocation,
		QStandardPaths.HomeLocation,
		QStandardPaths.DataLocation,
		QStandardPaths.AppLocalDataLocation,
		QStandardPaths.CacheLocation,
		QStandardPaths.GenericDataLocation,
		QStandardPaths.RuntimeLocation,
		QStandardPaths.ConfigLocation,
		QStandardPaths.DownloadLocation,
		QStandardPaths.GenericCacheLocation,
		QStandardPaths.GenericConfigLocation,
		QStandardPaths.AppDataLocation,
		QStandardPaths.AppConfigLocation]

for i, path in enumerate(std_paths_list):
	print(f'{path} {std_paths_list_names[i]} = {QStandardPaths.writableLocation(path)}')
