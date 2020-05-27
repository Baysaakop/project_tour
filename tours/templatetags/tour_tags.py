from django import template

register = template.Library()

@register.filter
def of_tour(images, tour):
    return images.filter(tour=tour).first().image.url

@register.filter
def in_tour(prices, tour):
    return prices.filter(tour=tour)

@register.filter
def get_min(prices, tour):
    targetlist = prices.filter(tour=tour)    
    min = 10000
    for t in targetlist:
        p = int(t.price_per)
        if p < min:
            min = p
                  
    return min

@register.filter
def plus(price):
    return price + 100;