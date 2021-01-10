from django import forms # 장고에서 제공하는 forms 기능을 사용하기 위해
from .models import Post,User # Post 모델을 사용하기 위해 import

class PostForm(forms.ModelForm): # PostForm이라는 이름의 모델폼 클래스 생성
    class Meta:
        model = Post # form에서 사용할 모델이 Post임을 명시
        image=forms.ImageField()
        fields = ['title','charge','max','min','date','criteria','content','image']

        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : '대회명을 입력해주세요.',
                }
            ),
            'charge' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : '참가비용을 입력해주세요.',
                }
            ),
            'max' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : '최대 참가인원을 입력해주세요.',
                }
            ),
            'min' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : '최소 참가인원을 입력해주세요.',
                }
            ),
            'date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date',
                }
            ),
            'criteria' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'textarea',
                }
            ),
            'content' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'textarea',
                }
            ),
            'image' : forms.FileInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'file',
                }
            ),

        }

