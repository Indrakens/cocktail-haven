from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    def cocktails(request):    
        context = {'recipes_list': recipes_list}

        return render(request, 'index.html')
            

class RecipeDetail(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        cocktail = get_object_or_404(queryset, slug=slug)
        comments = cocktail.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if cocktail.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe.html",
            {
                "cocktail": cocktail,
                "comments": comments,
                "commented": False, 
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        cocktail = get_object_or_404(queryset, slug=slug)
        comments = cocktail.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if cocktail.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.cocktail = cocktail
            comment.save()
        else:
            comment_form = CommentForm()        

        return render(
            request,
            "recipe.html",
            {
                "cocktail": cocktail,
                "comments": comments,
                "commented": True, 
                "liked": liked,
                "comment_form": CommentForm()
            },
        ) 


class RecipeLike(LoginRequiredMixin, View):
    
    def post(self, request, slug, *args, **kwargs):
        cocktail = get_object_or_404(Recipe, slug=slug)
        if cocktail.likes.filter(id=request.user.id).exists():
            cocktail.likes.remove(request.user)
        else:
            cocktail.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe', args=[slug]))


class CreateRecipe(LoginRequiredMixin, generic.CreateView):
    def createRecipe(request):
        form = RecipeForm()

        if request.method == 'POST':
            form = RecipeForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('home')

        context = {'form': form}
        return render(request, 'add-cocktail-form.html', context)        
