# django-to-Yapi

# 批量将Django Viewset视图接口导入Yapi 
  ## 1、drf_meta_data.py:对drf接口元数据的补充，主要补充了可排序字段和过滤字段，需要将SimpleMetadataWithFilters配置到django配置文件中
  ## 2、yapi.py：主程序，对django每个路由做options请求，拿到接口元数据，调用yapi接口来创建接口文档
