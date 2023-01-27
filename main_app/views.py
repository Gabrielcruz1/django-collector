from django.shortcuts import render

from django.http import HttpResponse #CLASS HANDLES SENDING A TYPE OF RESPONSE

from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView
from .models import Band


# bands = [
# Band("The Red Hot Chilli Peppers", "https://cdn.suwalls.com/wallpapers/music/red-hot-chili-peppers-with-helmets-51611-1920x1080.jpg","Red Hot Chili Peppers are an American rock band formed in Los Angeles in 1982, comprising vocalist Anthony Kiedis, bassist Flea, drummer Chad Smith, and guitarist John Frusciante. Their music incorporates elements of alternative rock, funk, punk rock, hard rock, hip hop, and psychedelic rock"),
# Band("Black Sabbath","https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2010/2/17/1266424365020/black-sabbath-rock-band-001.jpg?width=465&quality=85&dpr=1&s=none", "Black Sabbath were an English rock band, formed in Birmingham in 1968, by guitarist and main songwriter Tony Iommi, bassist and main lyricist Geezer Butler, drummer Bill Ward and singer Ozzy Osbourne. Black Sabbath are often cited as pioneers of heavy metal music."),
# Band("Led Zeppelin", "https://media.newyorker.com/photos/61e9b6a440b49e277739c9d9/master/w_2560%2Cc_limit/220131_r39778_rd.jpg", "Led Zeppelin were an English rock band formed in London in 1968. The group comprised vocalist Robert Plant, guitarist Jimmy Page, bassist/keyboardist John Paul Jones, and drummer John Bonham."),
# Band("Pink Floyd","https://www.clashmusic.com/wp-content/uploads/2020/06/Pink-Floyd-NPA837A-8-Photographer-Storm-Thorgerson-%C2%A9Pink-Floyd-Music-Ltd.jpg","Pink Floyd are an English rock band formed in London in 1965. Gaining an early following as one of the first British psychedelic groups, they were distinguished by their extended compositions, sonic experimentation, philosophical lyrics and elaborate live shows."),
# Band("The Rolling Stones", "https://media.gq-magazine.co.uk/photos/5d1396d42881cc0f290a823c/master/pass/rolling-stones-hp-02-gq-22feb16_iconic-images-terry-oneill_b.jpg", "The Rolling Stones are a British rock group, formed in 1962, that drew on Chicago blues stylings to create a unique vision of the dark side of post-1960s counterculture. The original members were Mick Jagger, Keith Richards, Brian Jones, Bill Wyman, and Charlie Watts."),
# Band("Sublime","https://consequence.net/wp-content/uploads/2021/11/sublime-pawn-shop-origins-photo-by-john-dunne.jpg?quality=80&w=1031&h=580&crop=1&resize=1031%2C580&strip", "Sublime was an American reggae rock and ska punk band from Long Beach, California, formed in 1988.[1] The band's line-up, consistent throughout its duration, consisted of Bradley Nowell (vocals and guitar), Eric Wilson (bass), and Bud Gaugh (drums)"),
# Band("Kings of Leon","https://o.aolcdn.com/images/dar/5845cadfecd996e0372f/5c33e5cee347f3dc8e29ecb921c265cc9205296a/aHR0cDovL3d3dy5ibG9nY2RuLmNvbS93d3cuam95c3RpcS5jb20vbWVkaWEvMjAwOS8wNy9raW5nc29mbGVvbjA3MTYwOS5qcGc=", "Kings of Leon is an American rock band formed in Nashville, Tennessee, in 1999. The band is composed of brothers Caleb, Nathan and Jared Followill, and their cousin Matthew Followill. Mt. Juliet, Tennessee, U.S."),
# ]


class Album:
    def __init__(self, band, title):
        self.band = band 
        self.title = title


albums = [ 
    Album("The Red Hot Chilli Peppers", "Stadium Arcadium"),
    Album("Black Sabbath", "Iron Man"),
    Album("Led Zeppelin", "Physical Graffiti"),
    Album("Pink Floyd", "Wish You Were Here"),
    Album("The Rolling Stones", "Tattoo You"),
    Album("Sublime", "40 Oz. To Freedom"),
    Album("Kings of Leon", "Mechanical Bull")

]



# Create your views here.

#UPDATED HOME CLASS TO EXTEND TEMPLATEVIEW
class Home(TemplateView):
    template_name = "home.html"

#UPDATED ABOUT CLASS TO EXTEND TEMPLATEVIEW
class About(TemplateView):
    template_name = "about.html"


class BandList(TemplateView):
    template_name = "band_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["bands"] = bands # this is where we add the key into our context object for the view to use
        name = self.request.GET.get("name")
        if name != None:
            context["band"] = Band.objects.filter(name__icontains=name) # USING THE MODEL TO QUERY THE DATABASE
            context["header"] = f"Searching for {name}"
        else:
            context["band"] = Band.objects.all()
            context["header"] = "Trending Bands"
        return context


#CRUD BELOW
class BandCreate(CreateView):
    model = Band
    fields = ['name', 'image', 'bio', 'verified_band']
    template_name = "band_create.html"
    success_url = "/bands/"


class AlbumList(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = albums
        return albums