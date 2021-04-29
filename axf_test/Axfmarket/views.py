from django.shortcuts import render

# Create your views here.
from Axfmarket.models import AxfFoodType, AxfGoods


# 全部分类: 0  # 酸奶乳菌:103537#牛奶豆浆103538
def market(request):
    typeid = request.GET.get('typeid', '104749')
    a_foodtype = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames
    c = a_foodtype.split('#')
    type_list_c = []
    for c_list in c:
        type_list_c.append(c_list.split(':'))

    childid = request.GET.get('childid','0')
    foodtypes = AxfFoodType.objects.all()
    goods_list = AxfGoods.objects
    if childid == '0':
        goods_list = goods_list.filter(categoryid=typeid)
    else:
        goods_list = goods_list.filter(childcid=childid)

    sort_rule = [
        ['综合排序', '0'],
        ['销售排序', '1'],
        ['价格降序', '2'],
        ['价格升序', '3'],
    ]

    sort_r_id = request.GET.get('sort_rule_id', '0')
    if sort_r_id == '0':
        pass
    elif sort_r_id == '1':
        goods_list = goods_list.order_by('-productnum')

    elif sort_r_id == '2':
        goods_list = goods_list.order_by('-price')

    elif sort_r_id == '3':
        goods_list = goods_list.order_by('price')


    context = {
        'foodtypes': foodtypes,
        'goods': goods_list,
        'typeid': typeid,
        'type_list': type_list_c,
        'childid': childid,
        'sort_rule': sort_rule,
        'sort_r_id': sort_r_id,
    }
    return render(request, 'axf/main/market/market.html', context=context)
