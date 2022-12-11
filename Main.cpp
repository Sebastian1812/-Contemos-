//	PROYECTO_FINAL_VIDEOJUEGO_CONTEMOS
//	REALIZAR UN VIDEOJUEGO LÚDICO QUE CONSISTE EN RESOLVER PROBLEMAS MATEMÁTICOS CONTANDO CON UN GATO
//	368327			Estefania Tello Mendoza
//	368366			Sebastian Jimenez Rojas
//	15/12/2022

#include <iostream>
#include <Windows.h>
#include <sstream>

#include <allegro5/allegro.h>
#include <allegro5/allegro_native_dialog.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>
#include <allegro5/allegro_primitives.h>
#include <allegro5/allegro_primitives.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_audio.h>
#include <allegro5/allegro_acodec.h>

#include <stdlib.h>
#include <string>
#include <time.h>


//#include "Fanny_Sebas.h" 

void jugar(ALLEGRO_COLOR negro, ALLEGRO_BITMAP* fondo_juego, ALLEGRO_EVENT_QUEUE* queue, ALLEGRO_DISPLAY* ventana);
void tiempo(ALLEGRO_EVENT_QUEUE* queue, ALLEGRO_EVENT evento, int segfin);
void usarTeclado(ALLEGRO_DISPLAY* ventana);
void numeros(int n1, int n2);

using namespace std;

void numeros(int n1, int n2)
{
	ALLEGRO_FONT* Golden_Age_Shad;
	ALLEGRO_COLOR azul = al_map_rgb(53, 43, 255);
	Golden_Age_Shad = al_load_font("Fuentes/Golden Age Shad.ttf", 80, 0);
	al_draw_text(Golden_Age_Shad, azul, 185, 275, NULL, (to_string(n1)).c_str());
	al_draw_text(Golden_Age_Shad, azul, 520, 275, NULL, (to_string(n2)).c_str());
}

void usarTeclado(ALLEGRO_DISPLAY* ventana)
{
	srand(time(NULL));
	

	ALLEGRO_TIMER* tiempo = al_create_timer(1.0 / 5);
	ALLEGRO_EVENT_QUEUE* evento_queue = al_create_event_queue();
	ALLEGRO_BITMAP* caminando[8];
	ALLEGRO_BITMAP* fondo[2];
	ALLEGRO_KEYBOARD_STATE keyState;

	al_register_event_source(evento_queue, al_get_keyboard_event_source());
	al_register_event_source(evento_queue, al_get_timer_event_source(tiempo));
	al_get_keyboard_state(&keyState);
	//no declarar variables antes del tiempo
	al_start_timer(tiempo);

	bool terminado = false, dibujo = true, activo = false;
	int x = 24, y = 460, xbackground;
	xbackground = x;
	int velMovimiento = 183;
	int i, j, indice, resultado;
	indice = 0, j = 0;
	float camaraPos[2] = { 0,0 };
	int n1, n2;
	int rf = 5;
	n1 = rand() % rf + 1;
	n2 = rand() % rf + 1;
	resultado = n1 + n2;
	numeros(n1, n2);


	for (i = 0; i < 8; i++)
	{
		std::stringstream str;
		str << "Imagenes/Gato/Gsptrite/Gato/" << i + 1 << ".png";
		caminando[i] = al_load_bitmap(str.str().c_str());
	}

	for (j = 0; j < 2; j++)
	{
		std::stringstream str;
		str << "Imagenes/Fondo/juego/" << j + 1 << ".png";
		fondo[j] = al_load_bitmap(str.str().c_str());
	}
	j = 0;

	while (!terminado)
	{
		ALLEGRO_EVENT eventos;
		al_wait_for_event(evento_queue, &eventos);

		if (eventos.type == ALLEGRO_EVENT_KEY_DOWN)
		{
			switch (eventos.keyboard.keycode)
			{
			case ALLEGRO_KEY_RIGHT:
				x += velMovimiento;
				xbackground += velMovimiento;
				if (x >= 1100)
				{
					x = 24;
				}
				if (xbackground < 1100)
				{
					j = 0;
					
				}
				else
				{
					j = 1;
					if (xbackground > 2200)
					{
						j = 0;
						xbackground = 24;
					}
				}
				break;
			case ALLEGRO_KEY_LEFT:
				x -= velMovimiento;
				xbackground -= velMovimiento;
				if (x < 24)
				{
					x = 24;
				}
				break;
			case ALLEGRO_KEY_ESCAPE:
				terminado = true;
				break;
			}
		}

		if (eventos.type == ALLEGRO_EVENT_DISPLAY_CLOSE)
		{
			terminado = true;
		}
		else
		{
			if (eventos.type == ALLEGRO_EVENT_TIMER)
			{
				activo = true;
				if (al_key_down(&keyState, ALLEGRO_KEY_RIGHT))
				{
					x += velMovimiento;
				}
			}
			else
			{
				activo = false;
			}

			if (activo)
			{
				indice++;
				if (indice >= 8)
				{
					indice = 0;
				}
			}
			dibujo = true;

		}
		if (dibujo)
		{
			numeros(n1,n2);
			al_draw_bitmap(caminando[indice], x, y, NULL);
			al_flip_display();
			al_draw_bitmap(fondo[j], 0, 0, 0);
			//al_clear_to_color(negro);
		}
	}
	al_destroy_display(ventana);
	for (i = 0; i < 8; i++)
	{
		al_destroy_bitmap(caminando[i]);
	}
	al_destroy_event_queue(evento_queue);
	al_destroy_bitmap(fondo[j]);


	cout << "Presionaste JUGAR HAHAHAHAHAHAHHAHAHA\n";
}

void jugar(ALLEGRO_COLOR negro, ALLEGRO_BITMAP* fondo_juego, ALLEGRO_EVENT_QUEUE* queue, ALLEGRO_DISPLAY* ventana)
{
	cout << "Presionaste JUGAR HOLA\n";
	while (true)
	{
		ALLEGRO_EVENT evento;
		al_wait_for_event(queue, &evento);
		al_clear_to_color(negro);
		al_draw_bitmap(fondo_juego, 0, 0, 0);
		usarTeclado(ventana);
		al_flip_display();
	}

}

void tiempo(ALLEGRO_EVENT_QUEUE* queue, ALLEGRO_EVENT evento, int segfin)
{
	ALLEGRO_TIMER* segundoTimer = al_create_timer(1.0);
	int segundo = 0;
	al_register_event_source(queue, al_get_timer_event_source(segundoTimer));
	al_start_timer(segundoTimer);
	al_stop_timer(segundoTimer);
	while (segundo < segfin)
	{
		if (evento.type == ALLEGRO_EVENT_TIMER)
		{
			if (evento.timer.source == segundoTimer)
			{
				segundo++;
				printf("%d\n", segundo);
				if (segundo == 10)
				{
					al_stop_timer(segundoTimer);
					al_start_timer(segundoTimer);
					segundo = 0;
				}
			}
		}
	}

}

int main()
{
	if (!al_init())
	{
		al_show_native_message_box(NULL, "ERROR CRITICO", "ERROR:404", "No se pudo cargar correctamente", NULL, ALLEGRO_MESSAGEBOX_ERROR);
		return -1;
	}
	al_init_font_addon();
	al_init_ttf_addon();
	al_init_primitives_addon();
	al_init_image_addon();
	al_install_mouse();
	al_install_keyboard();
	al_install_audio();
	al_init_acodec_addon();


	bool end_program = true;
	int alto = 700, ancho = 1106;
	int segundo = 0;
	//int countFPS = 0;
	int x = -1, y = -1;

	al_reserve_samples(1);

	ALLEGRO_SAMPLE* soundEffect = al_load_sample("Musica/boton.wav");
	ALLEGRO_SAMPLE* song = al_load_sample("Musica/musciakids.mp3");

	ALLEGRO_SAMPLE_INSTANCE* songInstance = al_create_sample_instance(song);
	al_set_sample_instance_playmode(songInstance, ALLEGRO_PLAYMODE_LOOP);
	al_attach_sample_instance_to_mixer(songInstance, al_get_default_mixer());


	ALLEGRO_DISPLAY* ventana = al_create_display(ancho, alto);
	ALLEGRO_EVENT_QUEUE* queue = al_create_event_queue();
	ALLEGRO_FONT* GAN = al_load_font("Fuentes/Golden Age Shad.ttf", 70, 0);
	ALLEGRO_FONT* GANbot = al_load_font("Fuentes/Golden Age Shad.ttf", 35, 0);

	int ancho_W = GetSystemMetrics(SM_CXSCREEN);
	int alto_W = GetSystemMetrics(SM_CYSCREEN);

	ALLEGRO_BITMAP* menu_null = al_load_bitmap("Imagenes/Fondo/background.png");
	ALLEGRO_BITMAP* menu_start = al_load_bitmap("Imagenes/Fondo/background_jugar.png");
	ALLEGRO_BITMAP* menu_start_1 = al_load_bitmap("Imagenes/Fondo/background_jugar_1.png");
	ALLEGRO_BITMAP* menu_exit = al_load_bitmap("Imagenes/Fondo/background_salir.png");
	ALLEGRO_BITMAP* menu_exit_1 = al_load_bitmap("Imagenes/Fondo/background_salir_1.png");
	ALLEGRO_BITMAP* fondo_juego = al_load_bitmap("Imagenes/Fondo/bg_fondcaja.png");

	//ALLEGRO_TIMER* fps = al_create_timer(1.0 / 30);

	al_set_window_title(ventana, "Contemos!");

	al_set_window_position(ventana, ancho_W / 2 - ancho / 2, alto_W / 2 - alto / 2);

	ALLEGRO_COLOR blanco = al_map_rgb(255, 255, 255);
	ALLEGRO_COLOR negro = al_map_rgb(0, 0, 0);
	ALLEGRO_COLOR rojo = al_map_rgb(255, 0, 0);


	//al_register_event_source(queue, al_get_timer_event_source(fps));
	al_register_event_source(queue, al_get_mouse_event_source());
	al_register_event_source(queue, al_get_keyboard_event_source());

	//al_start_timer(fps);

	al_play_sample_instance(songInstance);

	while (end_program == true)
	{
		ALLEGRO_EVENT evento;
		al_wait_for_event(queue, &evento);
		al_clear_to_color(negro);



		if (evento.type == ALLEGRO_EVENT_MOUSE_AXES || evento.type == ALLEGRO_EVENT_MOUSE_BUTTON_DOWN)
		{
			x = evento.mouse.x;
			y = evento.mouse.y;

			if (x >= 704 && x <= 976 && y >= 398 && y <= 475)
			{
				al_draw_bitmap(menu_start_1, 0, 0, 0);
				if (evento.mouse.button & 1)
				{
					al_draw_bitmap(menu_start, 0, 0, 0);
					al_play_sample(soundEffect, 1.0, 0.0, 1.0, ALLEGRO_PLAYMODE_ONCE, 0);
					jugar(negro, fondo_juego, queue, ventana);

				}
				else
				{
					al_draw_bitmap(menu_start_1, 0, 0, 0);
				}
			}
			else
			{
				if (x >= 704 && x <= 976 && y >= 529 && y <= 607)
				{

					al_draw_bitmap(menu_exit_1, 0, 0, 0);
					if (evento.mouse.button & 1)
					{
						al_draw_bitmap(menu_exit, 0, 0, 0);
						al_play_sample(soundEffect, 1.0, 0.0, 1.0, ALLEGRO_PLAYMODE_ONCE, 0);
						cout << "Presionaste SALIR\n";
						end_program = false;
					}
					else
					{
						al_draw_bitmap(menu_exit_1, 0, 0, 0);
					}
				}
				else
				{
					al_draw_bitmap(menu_null, 0, 0, 0);
				}
			}


		}
		else
		{
			al_draw_bitmap(menu_null, 0, 0, 0);
		}

		al_flip_display();
	}

	al_destroy_sample(soundEffect);
	al_destroy_sample_instance(songInstance);

	return 0;
}