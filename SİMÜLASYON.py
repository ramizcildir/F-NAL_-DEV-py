
import pygame
import numpy as np

# Kütle sınıfı
class mass():
    instances = []
    # Başlangıç konumu ,kütlesi ve kütlenin ilk hızını grektiren nesneyi başlat
    def __init__(self, x, y, mass, init_vx, init_vy):
        self.__class__.instances.append(self)
        self.x = x
        self.y = y
        self.mass = mass
        self.colour = RED 
        self.radius = 20 # Tüm kütlelerin çizileceği piksel yarıçaplarını ayarlar
        self.vx = init_vx
        self.vy = init_vy
        # Bu kütleye bağlı tüm yayların bir listesini başlatır, bu kütleye bağlı bir yay nesnesi oluşturulduğunda eklene
        self.springs = []
    
    # Çağrıldığında penceredeki kütleyi çizer
    def draw(self, win):
        x = self.x * SCALE + (WIDTH / 2)
        y = self.y * SCALE + (HEIGHT / 2)
        pygame.draw.circle(win, self.colour, (x, y), self.radius)
    
    # Ana kütle tarafı fizik simülasyon döngüsü
    def update(self):
        # Kütle üzerindeki mevcut toplam kütleleri 0 olarak ayarlar
        fx_tot = 0
        fy_tot = 0
        # Kütleye bağlı tüm yayların üzerinden   geçer , o yayaın uygulandığı kuvveti alır. Ardından,
        # döndürdüğü değerlerin toplama eklenmesi veya toplamdan çıkarılması gerekip gerekmedğini belirler.
        # fx ve fy' nin tanımlama şekiltanımlanma şeklidir. Eğer kütle yayın nesnesi ise , kuvvetlerin toplama eklenmesi 
        # Eğer yayın kütlesi nesne2 ise o zaman dönen kuvvetler toplamdan çıkarılmalıdır.
        for i in self.springs:
            fx, fy = i.force()
            if self is i.object1:
                fx_tot += fx
                fy_tot += fy
            # Başlangıçtaki "if, was, elif " komutları aynı kütleye sahip iki kütlenin oluşturulduğunu seçer
            
            if self is i.object2: 
                fx_tot -= fx
                fy_tot -= fy
        # Kütlenin anlık ivmesini bulur
        ax = fx_tot / self.mass
        ay = fy_tot / self.mass
        # Kütlenin yeni hızını hesaplar
        self.vx += ax * TIMESTEP
        self.vy += ay * TIMESTEP
        # Kütlenin yeni konumunu hesaplar
        self.x += self.vx * TIMESTEP
        self.y += self.vy * TIMESTEP



# Sabit nokta sınıfı (yayların asılı olduğu yer)
class wall():
    instances = []
    # Başlangıç pozizyonunu gerektiren nesneyi başlat
    def __init__(self,x,y):
        self.__class__.instances.append(self)
        self.x = x
        self.y = y
        # Bu sabit noktaya bağlı tüm yayların listesini balatır, bu noktaya bağlı  bir yay nesnesi oluşturulduğunda ekle
        # Bu liste , bağlı olduğu bir nesnenin kütle olması durumunda yayın eklenecek bir şeye sahip olması dışında, kütle gibi bir şey için kullanılmaz
        self.springs = []
    
    # Çağrıldığında penceredeki noktayı çizer
    def draw(self, win):
        x = self.x * SCALE + (WIDTH / 2)
        y = self.y * SCALE + (HEIGHT / 2)
        pygame.draw.circle(win,WHITE, (x, y), 5) # Sabit noktalar BEYAZ olarak ayarlanmıştır



# Yay sınıfı
class spring():
    instances = []
    # bağladığı iki nesneyi , yayın sertliğini ve doğal uzunluğunu gerektiren nesneyi başlatır
    def __init__(self, object_1, object_2, stiffness, nat_len):
        self.__class__.instances.append(self)
        self.object1 = object_1
        self.object2 = object_2
        self.x1 = object_1.x
        self.x2 = object_2.x
        self.y1 = object_1.y
        self.y2 = object_2.y
        self.stiffness = stiffness
        self.nat_len = nat_len
        self.colour = BLACK # Yayların çizileceği renk
        # bu iki satır , yay nesnesinin kendisine bağlı KÜTLELERİ yaylar listesiNe ekler
        object_1.springs.append(self)
        object_2.springs.append(self)

    # çağrıldığında yay pencereye çizilir
    def draw(self,win):
        x1, x2 = self.x1 * SCALE + (WIDTH / 2), self.x2 * SCALE + (WIDTH / 2)
        y1, y2 = self.y1 * SCALE + (HEIGHT / 2), self.y2 * SCALE + (HEIGHT / 2)
        pygame.draw.line(win, self.colour, (x1, y1), (x2, y2), 2)
    
    # ANA yay fizik döngüsü
    
    def force(self):
        # Yayın toplam uzunluğunu hem x,y hem de toplam olarak bulur
        len_x = self.x2 - self.x1
        len_y = self.y2 - self.y1
        len_tot = np.sqrt(len_x**2 + len_y**2)
        # yayın mevcut uzunluğu ile doğal uzunluğu arasındaki farkı bulun
        dlen = len_tot - self.nat_len
        # yayın gerilme kuvvetini belirlemek için bu farkı kullan
        force = dlen * self.stiffness
        
        fx = force * (len_x / len_tot)
        fy = force * (len_y / len_tot)
        # geri dönüş kuvveti bileşenleri
        return fx, fy

    # Yayın konumu , bu adlandırıldığından potansiyel olarak haraket etmiş kitlelerle eşleşecek şekilde günceller 
    # sonra " mass.update()"
    
    
    def update(self):
        self.x1, self.x2 = self.object1.x, self.object2.x
        self.y1, self.y2 = self.object1.y, self.object2.y
    def update(self, object_1, object_2): 
        self.x1, self.x2 = object_1.x, object_2.x
        self.y1, self.y2 = object_1.y, object_2.y



pygame.init()


SCALE = 10        # simülasyonun yakınlaştırma faktörünü ayarlar
     
FPS = 60     # ekranı güncellenme hızını ayarlar

TIMESTEP = 0.05    # simülasyonun her yinelenmesinde geliştirilecek ayrık zaman dilimini ayarlar

WIDTH, HEIGHT = 800, 600  # Ekran boyutu

# Pygame penceresi oluşturun
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KÜTLE - YAY SİMÜLASYONU")

# RGB renkleri ayarlayın
WHITE = ((255, 255, 255))
BLACK = ((0, 0, 0))
RED = ((255, 0, 0))
BLUE = ((0, 0, 255))

# Çağrılacak ana fonksiyon
def main():
    # süre döngüsünü doğrular
    run = True

    # simülasyon hızını tanımlayan FPS ile sınırlayan saati başlatır
    clock = pygame.time.Clock()

    # Tanımlanan kütleler
    mass1 = mass(-3, 0, 20, 0, 1) 
    mass2 = mass(-10, 0, 5, 0, 0)  

    # sabit noktalar tanımlaması
    wall1 = wall(0,0)

    # Tanımlanan yaylar
    spring1 = spring(mass1, wall1, 10, 10)       
    spring2 = spring(mass1, mass2, 5, 8)
    spring3 = spring(mass2, wall1, 1, 10)

    # Sınıfların tüm örneklerinin listelerini genel olarak erişilebilir hale getirir
    masses = mass.instances
    walls = wall.instances
    springs = spring.instances

    # Simülasyon hesaplamalarının yapıldığı zaman yineleme döngüsü
    while run:
        # Saati uygun miktarda ilerletir
        clock.tick(FPS)
        # Önceki yinelemelerde oluşturulan nesneleri örtmek için pencereyi mavi ile doldur
        WIN.fill(BLUE)

        # Sabit noktaların tümünü ekrana çeker
        for i in walls:
            i.draw(WIN)

        # Kütleler listesindeki tüm yaylar arasında döngüler yapar
        for i in masses:
            # Kütle üzerindekitoplam kuvveti, kendisine bağlı tüm yaylarda bulunan hesaplamaları yapar
            # sonra kütlenin anlık hesaplamasını yapar
            # Daha sonra kütlenin konumunu ayarlanan TIMESTEP' e göre günceller
            i.update()
            # Draws the mass in its new position
            i.draw(WIN)

        # Yaylar listesineki tüm yaylar arasında döngüler yapar
        for i in springs:
            # Bağlı olduğu nesneler artık taşınmış olabileceğinden yayın uç noktalarını günceller 
            i.update(i.object1,i.object2)
            # Yeni yayı çizer
            i.draw(WIN)

        # Pencere kapatılırsa  "pygame" nin çalişmasını sağlar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # ekranı güncelletin
        pygame.display.update()

    # Döngü kapatılan pencere tarafından kırıldığında "pygame" den çıkar
    pygame.quit()


main()


