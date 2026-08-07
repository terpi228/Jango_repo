from django import forms
from .models import Product

FORBIDDEN_WORDS = ['казино','криптовалюта','крипта','биржа','дешево','бесплатно','обман','полиция','радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        desc = cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word.lower() in (name or '').lower():
                raise forms.ValidationError(f'Название содержит запрещённое слово: "{word}"')
            if word.lower() in (desc or '').lower():
                raise forms.ValidationError(f'Описание содержит запрещённое слово: "{word}"')
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы Bootstrap ко всем полям
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Размер файла не должен превышать 5 МБ.')
            ext = image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError('Допустимы только форматы JPEG и PNG.')
        return image    