"""Récupération périodique des données."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)


class MonCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Lit les données à intervalle régulier et les partage entre les entités."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        super().__init__(
            hass, _LOGGER, config_entry=entry, name=DOMAIN, update_interval=DEFAULT_SCAN_INTERVAL
        )

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            # TODO : remplacer par l'appel réel (toujours en async, jamais de requests bloquant)
            # session = async_get_clientsession(self.hass)
            # async with session.get(URL, timeout=30) as resp: ...
            return {"value": 42}
        except Exception as err:  # noqa: BLE001
            raise UpdateFailed(str(err)) from err
