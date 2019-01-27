from django.shortcuts import redirect

class AdminGroupRequired:
    redirect_url = ''

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(
            [
                'product_detail.add_product',
                'product_detail.change_product',
                'product_detail.delete_product',
            ]
        ):
            return super(AdminGroupRequired, self).dispatch(request, *args, **kwargs)
        
        return redirect(self.redirect_url)