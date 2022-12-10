#include <iostream>
#include <allegro5/allegro.h>
#include <stdlib.h>
#include <allegro5/allegro_native_dialog.h>
#include <allegro5/allegro_font.h>
#include <allegro5/allegro_ttf.h>
#include <allegro5/allegro_primitives.h>
#include <string>
#include <allegro5/allegro_primitives.h>
#include <allegro5/allegro_image.h>
#include <Windows.h>
#include <sstream>
#include <time.h>

#include "Fanny_Sebas.h" 

void jugar(ALLEGRO_COLOR negro, ALLEGRO_BITMAP* fondo_juego, ALLEGRO_EVENT_QUEUE* queue, ALLEGRO_DISPLAY* ventana);
void tiempo(ALLEGRO_EVENT_QUEUE* queue, ALLEGRO_EVENT evento, int segfin);
void usarTeclado(ALLEGRO_DISPLAY* ventana);

using namespace std;

void usarTeclado(ALLEGRO_DISPLAY* ventana)
{
	ALLEGRO_BITMAP* buffer = al_load_bitmap("Imagenes/Fondo/bg_fondcaja.png");
	ALLEGRO_TIMER* tiempo = al_create_timer(1.0 / 5);
	ALLEGRO_EVENT_QUEUE* evento_queue = al_create_event_queue();
	ALLEGRO_BITMAP* caminando[8];
	ALLEGRO_KEYBOARD_STATE keyState;

	al_register_event_source(evento_queue, al_get_keyboard_event_source());
	al_register_event_source(evento_queue, al_get_timer_event_source(tiempo));
	al_get_keyboard_state(&keyState);
	al_start_timer(tiempo);

	bool terminado = false, dibujo = true, activo = false;
	int x = 24, y = 460;
	int velMovimiento = 183;
	int i, indice, dirPrevia;
	indice = 0, dirPrevia = 0;
	float camaraPos[2] = { 0,0 };


	for (i = 0; i < 8; i++)
	{
		std::stringstream str;
		str << "Imagenes/Gato/Gsptrite/Gato/" << i + 1 << ".png";
		caminando[i] = al_load_bitmap(str.str().c_str());
	}


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
				if (x >= 1100)
				{
					x = 24;
				}
				break;
			case ALLEGRO_KEY_LEFT:
				x -= velMovimiento;
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
			numeros(4);
			al_draw_bitmap(caminando[indice], x, y, NULL);
			al_flip_display();
			al_draw_bitmap(buffer, 0, 0, 0);
			//al_clear_to_color(negro);
		}
	}
	al_destroy_display(ventana);
	for (i = 0; i < 8; i++)
	{
		al_destroy_bitmap(caminando[i]);
	}
	al_destroy_event_queue(evento_queue);
	al_destroy_bitmap(buffer);


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


	bool end_program = true;
	int alto = 700, ancho = 1106;
	int segundo = 0;
	//int countFPS = 0;
	int x = -1, y = -1;

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


		if (evento.type == ALLEGRO_EVENT_KEY_DOWN)
		{
			switch (evento.keyboard.keycode)
			{
			case ALLEGRO_KEY_DOWN:
				cout << "presionaste abajo\n";
				break;
			case ALLEGRO_KEY_UP:
				cout << "presionaste arriba\n";
				break;
			case ALLEGRO_KEY_ENTER:
			case ALLEGRO_KEY_PAD_ENTER:
				cout << "presionaste enter\n";
				break;

			default:
				break;
			}
		}

		al_flip_display();
	}

	return 0;
}