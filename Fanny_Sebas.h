#include <iostream>
#include<allegro5/allegro.h>
#include<stdlib.h>
#include <allegro5/allegro_native_dialog.h>
#include<allegro5/allegro_font.h>
#include<allegro5/allegro_ttf.h>
#include<allegro5/allegro_primitives.h>
#include<string>
#include<allegro5/allegro_primitives.h>
#include<allegro5/allegro_image.h>
#include<Windows.h>
#include<sstream>
#include<time.h>


void numeros(int rf)
{
	ALLEGRO_FONT* Golden_Age_Shad;
	ALLEGRO_COLOR azul = al_map_rgb(53, 43, 255);
	Golden_Age_Shad = al_load_font("fuentes/Golden_Age_Shad.otf", 80, 0);
	int n1, n2, n3;

	n1 = rand() % rf + 1;
	n2 = rand() % rf + 1;
	n3 = rand() % rf + 1;


	al_draw_text(Golden_Age_Shad, azul, 185, 275, NULL, to_string(n1).c_str());
	al_draw_text(Golden_Age_Shad, azul, 520, 275, NULL, to_string(n2).c_str());
	al_draw_text(Golden_Age_Shad, azul, 875, 275, NULL, to_string(n3).c_str());
}