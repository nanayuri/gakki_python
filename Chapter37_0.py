
class Tickit_price:
    def calc_price(self):
        self.weekp_ad = 100
        self.weekend_ad = self.weekp_ad * 1.2
        self.child_wp = self.weekp_ad * 0.5
        self.child_wkd = self.weekend_ad * 0.5
        return 2 * self.weekp_ad + self.child_wp


p = Tickit_price()
print(p.calc_price())
