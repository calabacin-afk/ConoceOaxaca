"""Curated, source-backed records for presenting the Oaxaca catalogue."""

from datetime import UTC, datetime
from pathlib import Path

from flask import current_app

from ..constants import CATEGORIES
from ..extensions import get_catalog_collection


DEMO_PLACES = (
    {
        "id": "demo-casa-oaxaca",
        "photo_url": "/static/images/demo/demo-casa-oaxaca.png",
        "name": "Casa Oaxaca El Restaurante",
        "description": (
            "Restaurante de cocina oaxaqueña con menú inspirado en ingredientes "
            "y sabores locales. Cuenta con restaurante, bar y terraza; revisa su "
            "menú vigente y disponibilidad antes de asistir."
        ),
        "category": "gastronomia",
        "address": "Constitución 104-A, Centro, Oaxaca de Juárez, Oaxaca, C.P. 68000",
        "zone": "Centro",
        "website": "https://casaoaxacaelrestaurante.com/",
        "opening_hours": "Lunes a sábado 13:00–23:00; domingo 13:00–21:00",
        "price_min_mxn": 205,
        "price_max_mxn": 650,
        "price_basis": "published",
        "price_note": (
            "Rango de platillos publicado en la carta del restaurante; no representa "
            "el costo total por persona. Confirma la carta vigente."
        ),
        "price_source_url": (
            "https://casaoaxacaelrestaurante.com/wp-content/uploads/2025/11/"
            "MENU-CASA-OAXACA-web.pdf"
        ),
        "ambience": ["animado"],
        "companions": ["pareja", "amigos", "familia"],
        "tags": ["cocina oaxaqueña", "restaurante", "terraza"],
        "source_url": "https://casaoaxacaelrestaurante.com/",
    },
    {
        "id": "demo-cafe-brujula-santo-domingo",
        "photo_url": "/static/images/demo/demo-cafe-brujula-santo-domingo.png",
        "name": "Café Brújula · Santo Domingo",
        "description": (
            "Sucursal de Café Brújula en Macedonio Alcalá, en el Centro Histórico. "
            "Su página destaca el café oaxaqueño y las vistas al templo de Santo "
            "Domingo y al andador turístico. El precio es un gasto orientativo de "
            "demo; la sucursal no publica su menú en línea."
        ),
        "category": "cafeterias",
        "address": "Macedonio Alcalá 407, Centro, Oaxaca de Juárez, Oaxaca",
        "zone": "Centro",
        "website": "https://cafebrujula.com/",
        "price_min_mxn": 45,
        "price_max_mxn": 180,
        "price_basis": "estimate",
        "price_note": "Estimación de demo por persona para bebida y acompañamiento; confirma el menú en la sucursal.",
        "ambience": ["tranquilo", "animado"],
        "companions": ["solo", "pareja", "amigos", "familia"],
        "tags": ["café oaxaqueño", "café de especialidad", "Centro Histórico"],
        "source_url": "https://cafebrujula.com/pages/sucursales-1",
    },
    {
        "id": "demo-mercado-benito-juarez",
        "photo_url": "/static/images/demo/demo-mercado-benito-juarez.png",
        "name": "Mercado Benito Juárez",
        "description": (
            "Mercado tradicional del Centro Histórico con productos de las regiones "
            "de Oaxaca, alimentos, bebidas, flores y artesanías. El rango de precio "
            "es un gasto estimado de demo para una compra o comida sencilla; cada "
            "puesto fija sus propios precios."
        ),
        "category": "mercados",
        "address": (
            "Entre Flores Magón, Las Casas, 20 de Noviembre y Aldama, "
            "Centro, Oaxaca de Juárez, Oaxaca"
        ),
        "zone": "Centro",
        "opening_hours": "Diario, 07:00–21:00 (horario publicado por SECTUR Oaxaca)",
        "price_min_mxn": 50,
        "price_max_mxn": 300,
        "price_basis": "estimate",
        "price_note": "Estimación de demo por persona para antojitos o una compra pequeña; varía por puesto.",
        "ambience": ["animado", "familiar"],
        "companions": ["solo", "pareja", "amigos", "familia"],
        "tags": ["mercado", "comercio local", "productos regionales"],
        "source_url": (
            "https://www.oaxaca.travel/index.php/es/mercados/mercado-benito-juarez-es"
        ),
    },
    {
        "id": "demo-mercado-artesanias",
        "photo_url": "/static/images/demo/demo-mercado-artesanias.png",
        "name": "Mercado de Artesanías José Perfecto García",
        "description": (
            "Mercado José Perfecto García, conocido como Mercado de Artesanías. "
            "Reúne textiles, tallas de madera, piezas de barro, cerámica, joyería, "
            "bordados y artículos de palma elaborados en comunidades oaxaqueñas. "
            "El presupuesto mostrado es una estimación de demo; el precio depende "
            "de la pieza y del taller."
        ),
        "category": "artesanias",
        "address": "Calle Ignacio Zaragoza, Centro, Oaxaca de Juárez, Oaxaca",
        "zone": "Centro",
        "opening_hours": "Lunes a domingo, 09:00–19:00 (horario publicado por SECTUR Oaxaca)",
        "price_min_mxn": 100,
        "price_max_mxn": 2000,
        "price_basis": "estimate",
        "price_note": "Presupuesto de compra estimado para la demo; cada pieza tiene precio propio.",
        "ambience": ["animado", "familiar"],
        "companions": ["pareja", "amigos", "familia"],
        "tags": ["textiles", "barro", "tallas de madera", "artesanía"],
        "source_url": "https://www.oaxaca.travel/index.php/es/mercados/mercado-de-artesanias",
    },
    {
        "id": "demo-museo-textil-oaxaca",
        "photo_url": "/static/images/demo/demo-museo-textil-oaxaca.png",
        "name": "Museo Textil de Oaxaca",
        "description": (
            "Espacio para conocer textiles de Oaxaca, México y otras partes del mundo. "
            "La entrada es libre y el museo ofrece recorridos guiados gratuitos en "
            "español los miércoles a las 17:00; consulta la fuente para confirmar "
            "horarios y actividades vigentes."
        ),
        "category": "cultura",
        "address": "Av. Hidalgo 917, Centro Histórico, Oaxaca de Juárez, Oaxaca, C.P. 68000",
        "zone": "Centro",
        "website": "https://museotextildeoaxaca.org/",
        "opening_hours": (
            "Lunes a viernes 10:00–20:00; sábado 11:00–20:00; domingo 11:00–18:00"
        ),
        "price_min_mxn": 0,
        "price_max_mxn": 0,
        "price_basis": "published",
        "price_note": "Entrada libre según el museo. Los horarios y recorridos pueden cambiar.",
        "duration_minutes": 60,
        "ambience": ["tranquilo", "familiar"],
        "companions": ["solo", "pareja", "amigos", "familia"],
        "tags": ["museo", "textiles", "recorrido guiado", "entrada libre"],
        "source_url": "https://museotextildeoaxaca.org/visitanos/",
    },
    {
        "id": "demo-monte-alban",
        "photo_url": "/static/images/demo/demo-monte-alban.png",
        "name": "Zona Arqueológica de Monte Albán",
        "description": (
            "Antigua capital zapoteca reconocida como Patrimonio Mundial. El INAH "
            "describe su Plaza Principal, monumentos y larga ocupación. Su ficha "
            "publica admisión de $105 para visitantes nacionales y $210 para "
            "extranjeros; revisa descuentos y condiciones antes de ir."
        ),
        "category": "historia",
        "address": (
            "Camino Dr. Ignacio Bernal (a Monte Albán) s/n, "
            "Santa Cruz Xoxocotlán, Oaxaca"
        ),
        "zone": "Santa Cruz Xoxocotlán",
        "opening_hours": "Lunes a domingo 08:00–17:00; último acceso 16:00 (INAH)",
        "price_min_mxn": 105,
        "price_max_mxn": 210,
        "price_basis": "published",
        "price_note": "Tarifa INAH publicada: $105 MXN nacionales y $210 MXN extranjeros; revisa descuentos y días de entrada libre.",
        "ambience": ["aire-libre", "familiar"],
        "companions": ["pareja", "amigos", "familia"],
        "tags": ["zona arqueológica", "zapoteca", "Patrimonio Mundial", "INAH"],
        "source_url": "https://lugares.inah.gob.mx/es/node/4351",
    },
    {
        "id": "demo-hierve-el-agua",
        "photo_url": "/static/images/demo/demo-hierve-el-agua.png",
        "name": "Hierve el Agua",
        "description": (
            "Área natural con cascadas petrificadas, manantiales y pozas formadas "
            "por depósitos minerales. Se pueden recorrer senderos a pie o en "
            "bicicleta. La entrada comunitaria se reportó en $70 MXN durante 2026; "
            "estacionamiento y otros servicios pueden cobrarse aparte."
        ),
        "category": "naturaleza",
        "address": "San Isidro Roaguía, San Lorenzo Albarradas, Oaxaca",
        "price_min_mxn": 70,
        "price_max_mxn": 70,
        "price_basis": "reported",
        "price_note": "Precio reportado en 2026: $20 MXN de acceso por carretera y $50 MXN de entrada comunitaria. Confirma la tarifa y los cargos extra.",
        "price_source_url": (
            "https://oaxaca.eluniversal.com.mx/mas-de-oaxaca/semana-santa-2026-"
            "cuanto-cuesta-nadar-en-las-pozas-de-las-cascadas-petrificadas-de-"
            "hierve-el-agua/?outputType=amp"
        ),
        "ambience": ["aire-libre", "familiar"],
        "companions": ["pareja", "amigos", "familia"],
        "tags": ["cascadas petrificadas", "pozas", "caminata", "naturaleza"],
        "source_url": "https://oaxaca.travel/index.php/es/all-destinations-es/hierve-el-agua-es",
    },
    {
        "id": "demo-ruta-magica-artesanias",
        "photo_url": "/static/images/demo/demo-ruta-magica-artesanias.png",
        "name": "Ruta Mágica de las Artesanías · itinerario de un día",
        "description": (
            "Itinerario turístico de 12 horas con salida desde la ciudad de Oaxaca. "
            "La ruta estatal propone paradas en Santa María Atzompa, Zaachila, "
            "Ocotlán, San Antonino Castillo Velasco y San Martín Tilcajete. Es una "
            "propuesta de recorrido; transporte y visitas se coordinan por separado. "
            "El costo mostrado es un presupuesto estimado de demo, no una tarifa "
            "oficial ni una cotización de operadora."
        ),
        "category": "experiencias",
        "zone": "Valles Centrales de Oaxaca",
        "duration_minutes": 720,
        "price_min_mxn": 300,
        "price_max_mxn": 1500,
        "price_basis": "estimate",
        "price_note": "Estimación de demo por persona para transporte y accesos; comidas, compras y operadora pueden cambiar el total.",
        "ambience": ["aire-libre", "animado", "familiar"],
        "companions": ["pareja", "amigos", "familia"],
        "tags": ["itinerario", "artesanías", "Valles Centrales", "recorrido cultural"],
        "source_url": (
            "https://www.oaxaca.travel/index.php/es/sitios-de-interes-es/"
            "rutas-tursiticas-es/rutas-e-itinerarios/rutas-e-itinerarios/"
            "ruta-magica-de-las-artesanias-itinerario-1-dia"
        ),
    },
    {
        "id": "demo-modulo-informacion-turistica",
        "photo_url": "/static/images/demo/demo-modulo-informacion-turistica.png",
        "name": "Módulo de Información Turística de Oaxaca",
        "description": (
            "Servicio público de la Secretaría de Turismo de Oaxaca para solicitar "
            "orientación turística general. La ficha oficial indica atención gratuita "
            "y proporciona dirección y teléfono; confirma la ubicación del módulo "
            "antes de acudir."
        ),
        "category": "servicios",
        "address": "Av. Benito Juárez 703, Centro, Oaxaca de Juárez, Oaxaca, C.P. 68000",
        "zone": "Centro",
        "phone": "+52 951 502 1200 ext. 1203",
        "opening_hours": "Diario, 09:00–20:00 (horario publicado por SECTUR Oaxaca)",
        "price_min_mxn": 0,
        "price_max_mxn": 0,
        "price_basis": "published",
        "price_note": "Servicio de información turística gratuito según SECTUR Oaxaca.",
        "ambience": ["tranquilo"],
        "companions": ["solo", "pareja", "amigos", "familia"],
        "tags": ["información turística", "servicio público", "gratuito"],
        "source_url": "https://www.oaxaca.gob.mx/sectur/atencion-en-modulos-de-informacion/",
    },
)


def _document(place):
    parts = [place["name"], place["description"], CATEGORIES[place["category"]]]
    if place.get("zone"):
        parts.append(place["zone"])
    parts.extend(place.get("tags", []))
    return "\n".join(parts)


def _metadata(place, now, existing=None):
    metadata = {
        "name": place["name"],
        "description": place["description"],
        "category": place["category"],
        "status": "verificado",
        "embedding_status": "pendiente",
        "created_at": (existing or {}).get("created_at", now),
        "created_by": (existing or {}).get("created_by", "demo_seed"),
        "verified_by": "fuentes_oficiales",
        "verified_at": (existing or {}).get("verified_at", now),
        "demo_seed": "oaxaca-demo-v1",
        "source_url": place["source_url"],
    }
    for key in (
        "address",
        "zone",
        "phone",
        "website",
        "opening_hours",
        "duration_minutes",
        "price_min_mxn",
        "price_max_mxn",
        "price_basis",
        "price_note",
        "price_source_url",
    ):
        if place.get(key) is not None:
            metadata[key] = place[key]
    photo_url = place.get("photo_url")
    if photo_url:
        photo_path = Path(current_app.static_folder) / photo_url.removeprefix("/static/")
        if photo_path.is_file():
            metadata["photo_url"] = photo_url
            metadata["photo_is_ai"] = True
    for key in ("tags", "ambience", "companions"):
        if place.get(key):
            metadata[key] = place[key]
    return metadata


def seed_demo_places():
    """Add or refresh curated demo records without changing other catalogue data."""
    collection = get_catalog_collection()
    ids = [place["id"] for place in DEMO_PLACES]
    result = collection.get(ids=ids, include=["metadatas"])
    existing_by_id = dict(zip(result["ids"], result["metadatas"]))
    to_add = [place for place in DEMO_PLACES if place["id"] not in existing_by_id]
    to_update = [
        place
        for place in DEMO_PLACES
        if existing_by_id.get(place["id"], {}).get("demo_seed") == "oaxaca-demo-v1"
    ]
    protected = len(existing_by_id) - len(to_update)
    now = datetime.now(UTC).isoformat()

    if to_add:
        collection.add(
            ids=[place["id"] for place in to_add],
            embeddings=[[0.0] for _ in to_add],
            documents=[_document(place) for place in to_add],
            metadatas=[_metadata(place, now) for place in to_add],
        )
    if to_update:
        collection.update(
            ids=[place["id"] for place in to_update],
            embeddings=[[0.0] for _ in to_update],
            documents=[_document(place) for place in to_update],
            metadatas=[
                _metadata(place, now, existing_by_id[place["id"]])
                for place in to_update
            ],
        )
    return len(to_add), len(to_update), protected, collection.count()
